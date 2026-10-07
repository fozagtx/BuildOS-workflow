#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any


BASE_URL = os.environ.get("AI33_BASE_URL", "https://api.ai33.pro").rstrip("/")
ENV_FILES = (".env", ".env.local", "ai33.env")
KEY_NAMES = ("AI33_API_KEY", "XI_API_KEY", "AI33_XI_API_KEY")
RETRY_API_ATTEMPTS = int(os.environ.get("AI33_RETRY_API_ATTEMPTS", os.environ.get("AI33_RETRY_429_ATTEMPTS", "30")))
RETRY_API_SECONDS = float(os.environ.get("AI33_RETRY_API_SECONDS", os.environ.get("AI33_RETRY_429_SECONDS", "20")))
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}
VOICE_ID_PREFIXES = ("elevenlabs_", "minimax_", "clone_", "edge_", "kokoro_", "vbee_", "fishaudio_")


def load_env_files() -> None:
    roots: list[Path] = [Path.cwd(), Path(__file__).resolve().parent]
    seen: set[Path] = set()
    for root in roots:
        for parent in (root, *root.parents):
            for name in ENV_FILES:
                path = parent / name
                if path in seen or not path.exists() or not path.is_file():
                    continue
                seen.add(path)
                for raw in path.read_text(encoding="utf-8").splitlines():
                    line = raw.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = value
            if parent == Path.home():
                break


def api_key() -> str:
    load_env_files()
    for name in KEY_NAMES:
        value = os.environ.get(name)
        if value:
            return value
    raise SystemExit("Missing AI33 API key. Set AI33_API_KEY in your shell or in a local .env file.")


def json_print(data: Any) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def fail_from_http(exc: urllib.error.HTTPError) -> None:
    body = exc.read().decode("utf-8", errors="replace")
    raise SystemExit(f"AI33 API error {exc.code}: {body}") from exc


def retry_or_fail(exc: urllib.error.HTTPError, attempt: int) -> bool:
    body = exc.read().decode("utf-8", errors="replace")
    if exc.code in RETRYABLE_HTTP_CODES and attempt < RETRY_API_ATTEMPTS:
        print(
            f"AI33 API {exc.code}, waiting {RETRY_API_SECONDS:g}s before retry "
            f"{attempt + 1}/{RETRY_API_ATTEMPTS}: {body}",
            file=sys.stderr,
            flush=True,
        )
        time.sleep(RETRY_API_SECONDS)
        return True
    raise SystemExit(f"AI33 API error {exc.code}: {body}") from exc


def request_json(method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    url = f"{BASE_URL}{path}"
    data = None
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": api_key(),
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    text = ""
    for attempt in range(RETRY_API_ATTEMPTS + 1):
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                text = response.read().decode("utf-8")
            break
        except urllib.error.HTTPError as exc:
            if retry_or_fail(exc, attempt):
                continue
        except urllib.error.URLError as exc:
            raise SystemExit(f"AI33 request failed: {exc}") from exc
    return json.loads(text) if text else {}


def multipart_request(
    path: str,
    fields: dict[str, str],
    files: list[tuple[str, Path]] | None = None,
) -> dict[str, Any]:
    boundary = f"----ai33-{uuid.uuid4().hex}"
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks.append(f"--{boundary}\r\n".encode("utf-8"))
        chunks.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("utf-8"))
        chunks.append(str(value).encode("utf-8"))
        chunks.append(b"\r\n")
    for name, path_obj in files or []:
        content_type = mimetypes.guess_type(path_obj.name)[0] or "application/octet-stream"
        chunks.append(f"--{boundary}\r\n".encode("utf-8"))
        chunks.append(
            (
                f'Content-Disposition: form-data; name="{name}"; '
                f'filename="{path_obj.name}"\r\n'
                f"Content-Type: {content_type}\r\n\r\n"
            ).encode("utf-8")
        )
        chunks.append(path_obj.read_bytes())
        chunks.append(b"\r\n")
    chunks.append(f"--{boundary}--\r\n".encode("utf-8"))

    text = ""
    for attempt in range(RETRY_API_ATTEMPTS + 1):
        req = urllib.request.Request(
            f"{BASE_URL}{path}",
            data=b"".join(chunks),
            headers={
                "Content-Type": f"multipart/form-data; boundary={boundary}",
                "xi-api-key": api_key(),
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as response:
                text = response.read().decode("utf-8")
            break
        except urllib.error.HTTPError as exc:
            if retry_or_fail(exc, attempt):
                continue
        except urllib.error.URLError as exc:
            raise SystemExit(f"AI33 request failed: {exc}") from exc
    return json.loads(text) if text else {}


def read_text_arg(args: argparse.Namespace) -> str:
    if getattr(args, "text_file", None):
        return Path(args.text_file).read_text(encoding="utf-8").strip()
    if getattr(args, "text", None):
        return str(args.text).strip()
    raise SystemExit("Provide --text or --text-file.")


def require_prefixed_voice_id(voice_id: str) -> str:
    if not voice_id.startswith(VOICE_ID_PREFIXES):
        prefixes = ", ".join(VOICE_ID_PREFIXES)
        raise SystemExit(f"v3 voice_id must start with one of: {prefixes}")
    return voice_id


def bool_form(value: bool) -> str:
    return "true" if value else "false"


def add_optional_field(fields: dict[str, str], name: str, value: Any) -> None:
    if value is None:
        return
    fields[name] = str(value)


def read_json_arg(value: str | None, file_path: str | None, label: str) -> Any:
    if file_path:
        raw = Path(file_path).read_text(encoding="utf-8")
    elif value:
        raw = value
    else:
        raise SystemExit(f"Provide --{label} or --{label}-file.")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON for {label}: {exc}") from exc


def append_task_log(out_dir: Path | None, command: str, data: dict[str, Any]) -> None:
    if out_dir is None:
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    tasks_path = out_dir / "tasks.json"
    try:
        entries = json.loads(tasks_path.read_text(encoding="utf-8")) if tasks_path.exists() else []
    except json.JSONDecodeError:
        entries = []
    entries.append({"created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "command": command, "data": data})
    tasks_path.write_text(json.dumps(entries, indent=2), encoding="utf-8")


def get_task(task_id: str) -> dict[str, Any]:
    safe_id = urllib.parse.quote(task_id, safe="")
    return request_json("GET", f"/v1/task/{safe_id}")


def poll_task(task_id: str, interval: float, timeout: float) -> dict[str, Any]:
    started = time.time()
    while True:
        task = get_task(task_id)
        status = task.get("status")
        progress = task.get("progress")
        message = f"[poll] {task_id} status={status}"
        if progress is not None:
            message += f" progress={progress}"
        print(message, file=sys.stderr, flush=True)
        if status == "done":
            return task
        if status == "error":
            raise SystemExit(f"AI33 task failed: {task.get('error_message') or task}")
        if time.time() - started > timeout:
            raise SystemExit(f"Timed out waiting for AI33 task {task_id}")
        time.sleep(interval)


def suffix_from_url(url: str, default: str) -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix
    return suffix if suffix else default


def download_url(url: str, target: Path) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "ai33-client/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=300) as response:
            target.write_bytes(response.read())
    except urllib.error.URLError as exc:
        raise SystemExit(f"Download failed for {url}: {exc}") from exc
    print(f"[download] {target}", file=sys.stderr, flush=True)
    return target


def download_task_assets(task: dict[str, Any], out_dir: Path) -> list[str]:
    metadata = task.get("metadata") or {}
    task_type = str(task.get("type") or "")
    downloaded: list[str] = []

    for index, item in enumerate(metadata.get("result_images") or [], start=1):
        url = item.get("imageUrl") or item.get("previewUrl")
        if not url:
            continue
        target = out_dir / f"image-{index:02d}{suffix_from_url(url, '.png')}"
        downloaded.append(str(download_url(url, target)))

    audio_url = metadata.get("audio_url")
    if audio_url:
        audio_name = "voiceover.mp3" if task_type in {"tts", "minimax_tts", "dialogue", "text_to_dialogue"} or "tts" in task_type else "audio.mp3"
        downloaded.append(str(download_url(audio_url, out_dir / audio_name)))

    output_uri = metadata.get("output_uri") or task.get("output_uri")
    if output_uri:
        name = "sound-effect.mp3" if "sound" in task_type else f"output{suffix_from_url(output_uri, '.mp3')}"
        downloaded.append(str(download_url(output_uri, out_dir / name)))

    srt_url = metadata.get("srt_url")
    if srt_url:
        downloaded.append(str(download_url(srt_url, out_dir / "captions.srt")))

    json_url = metadata.get("json_url")
    if json_url:
        downloaded.append(str(download_url(json_url, out_dir / "transcript.json")))

    music_result = metadata.get("music_result") or {}
    for index, item in enumerate(music_result.get("data") or [], start=1):
        url = item.get("audio_url")
        if url:
            downloaded.append(str(download_url(url, out_dir / f"music-{index:02d}.mp3")))

    return downloaded


def task_id_from(data: dict[str, Any]) -> str:
    task_id = data.get("task_id") or data.get("id")
    if not task_id:
        raise SystemExit(f"AI33 response did not include task_id: {data}")
    return str(task_id)


def maybe_wait_and_download(args: argparse.Namespace, response: dict[str, Any], out_dir: Path | None) -> dict[str, Any]:
    if not getattr(args, "wait", False):
        return response
    task = poll_task(task_id_from(response), args.interval, args.timeout)
    if getattr(args, "download", False):
        if out_dir is None:
            raise SystemExit("--download requires --out-dir.")
        task["downloaded_files"] = download_task_assets(task, out_dir)
    return task


def cmd_health(_: argparse.Namespace) -> int:
    json_print(request_json("GET", "/v1/health-check"))
    return 0


def cmd_credits(_: argparse.Namespace) -> int:
    json_print(request_json("GET", "/v1/credits"))
    return 0


def cmd_models(args: argparse.Namespace) -> int:
    if args.provider == "image":
        json_print(request_json("GET", "/v1i/models"))
    elif args.provider == "minimax":
        json_print(request_json("GET", "/v1m/common/config"))
    else:
        json_print(request_json("GET", "/v1/models"))
    return 0


def cmd_voices(args: argparse.Namespace) -> int:
    provider = "elevenlabs" if args.provider == "eleven" else args.provider
    params: dict[str, str] = {
        "provider": provider,
        "page": str(args.page),
        "page_size": str(args.page_size),
    }
    for name in (
        "search",
        "q",
        "filters",
        "language",
        "locale",
        "gender",
        "age",
        "accent",
        "category",
        "use_case",
        "descriptive",
        "voice_ownership",
        "sort",
        "tag",
    ):
        add_optional_field(params, name, getattr(args, name, None))
    json_print(request_json("GET", f"/v3/voices?{urllib.parse.urlencode(params)}"))
    return 0


def cmd_image_price(args: argparse.Namespace) -> int:
    payload = {
        "model_id": args.model_id,
        "generations_count": args.generations_count,
        "model_parameters": {"aspect_ratio": args.aspect_ratio, "resolution": args.resolution},
        "assets": args.assets,
    }
    json_print(request_json("POST", "/v1i/task/price", payload))
    return 0


def cmd_image_generate(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir) if args.out_dir else None
    asset_paths = [Path(p) for p in args.assets]
    for path in asset_paths:
        if not path.exists():
            raise SystemExit(f"Asset not found: {path}")
    fields = {
        "prompt": read_text_arg(args),
        "model_id": args.model_id,
        "generations_count": str(args.generations_count),
        "model_parameters": json.dumps({"aspect_ratio": args.aspect_ratio, "resolution": args.resolution}),
    }
    if args.receive_url:
        fields["receive_url"] = args.receive_url
    if not args.no_price:
        price_payload = {
            "model_id": args.model_id,
            "generations_count": args.generations_count,
            "model_parameters": {"aspect_ratio": args.aspect_ratio, "resolution": args.resolution},
            "assets": len(asset_paths),
        }
        print(json.dumps(request_json("POST", "/v1i/task/price", price_payload)), file=sys.stderr)
    response = multipart_request("/v1i/task/generate-image", fields, [("assets", path) for path in asset_paths])
    append_task_log(out_dir, "image-generate", response)
    result = maybe_wait_and_download(args, response, out_dir)
    json_print(result)
    return 0


def cmd_tts(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir) if args.out_dir else None
    fields: dict[str, str] = {
        "text": read_text_arg(args),
        "voice_id": require_prefixed_voice_id(args.voice_id),
        "speed": str(args.speed),
        "with_transcript": bool_form(args.with_transcript),
    }
    if getattr(args, "context_chaining", False):
        fields["context_chaining"] = bool_form(args.context_chaining)
    add_optional_field(fields, "file_name", getattr(args, "file_name", None))
    add_optional_field(fields, "receive_url", getattr(args, "receive_url", None))
    add_optional_field(fields, "pronunciation_dictionary_id", getattr(args, "pronunciation_dictionary_id", None))
    response = multipart_request("/v3/text-to-speech", fields)
    append_task_log(out_dir, getattr(args, "command", "tts"), response)
    result = maybe_wait_and_download(args, response, out_dir)
    json_print(result)
    return 0


def cmd_dialogue(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir) if args.out_dir else None
    speakers = read_json_arg(args.speakers, args.speakers_file, "speakers")
    if not isinstance(speakers, list) or len(speakers) < 2:
        raise SystemExit("speakers must be a JSON array with at least two speakers.")
    for index, speaker in enumerate(speakers, start=1):
        if not isinstance(speaker, dict) or "voice_id" not in speaker:
            raise SystemExit(f"Speaker {index} must include voice_id.")
        require_prefixed_voice_id(str(speaker["voice_id"]))
    fields: dict[str, str] = {
        "text": read_text_arg(args),
        "speakers": json.dumps(speakers, ensure_ascii=False),
        "delay": str(args.delay),
        "with_transcript": bool_form(args.with_transcript),
    }
    if args.context_chaining:
        fields["context_chaining"] = bool_form(args.context_chaining)
    add_optional_field(fields, "file_name", args.file_name)
    add_optional_field(fields, "receive_url", args.receive_url)
    add_optional_field(fields, "pronunciation_dictionary_id", args.pronunciation_dictionary_id)
    response = multipart_request("/v3/text-to-speech/dialogue", fields)
    append_task_log(out_dir, "dialogue", response)
    result = maybe_wait_and_download(args, response, out_dir)
    json_print(result)
    return 0


def cmd_voice_clone(args: argparse.Namespace) -> int:
    audio_path = Path(args.audio_file)
    if not audio_path.exists():
        raise SystemExit(f"Audio file not found: {audio_path}")
    response = multipart_request(
        "/v3/text-to-speech/voice-clone",
        {"voice_name": args.voice_name},
        [("audio_file", audio_path)],
    )
    voice_id = ((response.get("data") or {}).get("voice_id") if isinstance(response.get("data"), dict) else None)
    if voice_id and "prefixed_voice_id" not in response:
        response["prefixed_voice_id"] = f"clone_{voice_id}"
    json_print(response)
    return 0


def cmd_voice_clone_delete(args: argparse.Namespace) -> int:
    safe_id = urllib.parse.quote(args.voice_clone_id, safe="")
    json_print(request_json("DELETE", f"/v3/text-to-speech/voice-clone/{safe_id}"))
    return 0


def dictionary_payload(args: argparse.Namespace, require_name: bool = False, require_rules: bool = False) -> dict[str, Any]:
    payload: dict[str, Any] = {}
    if getattr(args, "name", None):
        payload["name"] = args.name
    elif require_name:
        raise SystemExit("Provide --name.")
    if getattr(args, "rules", None) or getattr(args, "rules_file", None):
        rules = read_json_arg(args.rules, args.rules_file, "rules")
        if not isinstance(rules, list):
            raise SystemExit("rules must be a JSON array.")
        payload["rules"] = rules
    elif require_rules:
        raise SystemExit("Provide --rules or --rules-file.")
    return payload


def cmd_dictionary_list(_: argparse.Namespace) -> int:
    json_print(request_json("GET", "/v3/dictionaries"))
    return 0


def cmd_dictionary_get(args: argparse.Namespace) -> int:
    safe_id = urllib.parse.quote(str(args.dictionary_id), safe="")
    json_print(request_json("GET", f"/v3/dictionaries/{safe_id}"))
    return 0


def cmd_dictionary_create(args: argparse.Namespace) -> int:
    json_print(request_json("POST", "/v3/dictionaries", dictionary_payload(args, require_name=True, require_rules=True)))
    return 0


def cmd_dictionary_update(args: argparse.Namespace) -> int:
    safe_id = urllib.parse.quote(str(args.dictionary_id), safe="")
    payload = dictionary_payload(args)
    if not payload:
        raise SystemExit("Provide --name, --rules, or --rules-file.")
    json_print(request_json("PUT", f"/v3/dictionaries/{safe_id}", payload))
    return 0


def cmd_dictionary_delete(args: argparse.Namespace) -> int:
    safe_id = urllib.parse.quote(str(args.dictionary_id), safe="")
    json_print(request_json("DELETE", f"/v3/dictionaries/{safe_id}"))
    return 0


def cmd_dictionary_preview(args: argparse.Namespace) -> int:
    payload = {
        "text": read_text_arg(args),
        "rules": dictionary_payload(args, require_rules=True)["rules"],
    }
    json_print(request_json("POST", "/v3/dictionaries/preview", payload))
    return 0


def cmd_sound_effect(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir) if args.out_dir else None
    payload: dict[str, Any] = {
        "text": read_text_arg(args),
        "duration_seconds": args.duration_seconds,
        "prompt_influence": args.prompt_influence,
        "loop": args.loop,
        "model_id": args.model_id,
    }
    if args.receive_url:
        payload["receive_url"] = args.receive_url
    response = request_json("POST", "/v1/task/sound-effect", payload)
    append_task_log(out_dir, "sound-effect", response)
    result = maybe_wait_and_download(args, response, out_dir)
    json_print(result)
    return 0


def cmd_poll(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir) if args.out_dir else None
    task = poll_task(args.task_id, args.interval, args.timeout)
    if args.download:
        if out_dir is None:
            raise SystemExit("--download requires --out-dir.")
        task["downloaded_files"] = download_task_assets(task, out_dir)
    json_print(task)
    return 0


def cmd_list_tasks(args: argparse.Namespace) -> int:
    params = {"page": str(args.page), "limit": str(args.limit)}
    if args.type:
        params["type"] = args.type
    json_print(request_json("GET", f"/v1/tasks?{urllib.parse.urlencode(params)}"))
    return 0


def cmd_delete_tasks(args: argparse.Namespace) -> int:
    payload = {"task_ids": args.task_ids}
    json_print(request_json("POST", "/v1/task/delete", payload))
    return 0


def add_common_wait_flags(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--wait", action="store_true")
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--out-dir")
    parser.add_argument("--interval", type=float, default=5)
    parser.add_argument("--timeout", type=float, default=900)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI33 API client for YouTube Content Studio workflows.")
    sub = parser.add_subparsers(dest="command", required=True)

    health = sub.add_parser("health")
    health.set_defaults(func=cmd_health)

    credits = sub.add_parser("credits")
    credits.set_defaults(func=cmd_credits)

    models = sub.add_parser("models")
    models.add_argument("--provider", choices=["image", "minimax", "eleven"], default="image")
    models.set_defaults(func=cmd_models)

    voices = sub.add_parser("voices")
    voices.add_argument(
        "--provider",
        choices=["elevenlabs", "eleven", "minimax", "clone", "edge", "kokoro", "vbee", "fishaudio"],
        default="minimax",
    )
    voices.add_argument("--search")
    voices.add_argument("--q")
    voices.add_argument("--page", type=int, default=1)
    voices.add_argument("--page-size", type=int, default=30)
    voices.add_argument("--filters")
    voices.add_argument("--language")
    voices.add_argument("--locale")
    voices.add_argument("--gender")
    voices.add_argument("--age")
    voices.add_argument("--accent")
    voices.add_argument("--category")
    voices.add_argument("--use-case", dest="use_case")
    voices.add_argument("--descriptive")
    voices.add_argument("--voice-ownership", dest="voice_ownership")
    voices.add_argument("--sort", choices=["score", "task_count", "created_at", "trending"])
    voices.add_argument("--tag")
    voices.set_defaults(func=cmd_voices)

    image_price = sub.add_parser("image-price")
    image_price.add_argument("--model-id", default="bytedance-seedream-4.5")
    image_price.add_argument("--generations-count", type=int, default=1)
    image_price.add_argument("--aspect-ratio", default="16:9")
    image_price.add_argument("--resolution", default="2K")
    image_price.add_argument("--assets", type=int, default=0)
    image_price.set_defaults(func=cmd_image_price)

    image = sub.add_parser("image-generate")
    image.add_argument("--text")
    image.add_argument("--text-file")
    image.add_argument("--model-id", default="bytedance-seedream-4.5")
    image.add_argument("--generations-count", type=int, default=1)
    image.add_argument("--aspect-ratio", default="16:9")
    image.add_argument("--resolution", default="2K")
    image.add_argument("--receive-url")
    image.add_argument("--assets", action="append", default=[])
    image.add_argument("--no-price", action="store_true")
    add_common_wait_flags(image)
    image.set_defaults(func=cmd_image_generate)

    def add_tts_args(tts_parser: argparse.ArgumentParser) -> None:
        tts_parser.add_argument("--text")
        tts_parser.add_argument("--text-file")
        tts_parser.add_argument("--voice-id", required=True)
        tts_parser.add_argument("--speed", type=float, default=1)
        tts_parser.add_argument("--with-transcript", action="store_true")
        tts_parser.add_argument("--context-chaining", action="store_true")
        tts_parser.add_argument("--file-name")
        tts_parser.add_argument("--receive-url")
        tts_parser.add_argument("--pronunciation-dictionary-id", type=int)
        add_common_wait_flags(tts_parser)
        tts_parser.set_defaults(func=cmd_tts)

    tts = sub.add_parser("tts")
    add_tts_args(tts)

    minimax = sub.add_parser("minimax-tts", help="Alias for v3 tts; voice_id must be prefixed, e.g. minimax_...")
    add_tts_args(minimax)

    eleven = sub.add_parser("eleven-tts", help="Alias for v3 tts; voice_id must be prefixed, e.g. elevenlabs_...")
    add_tts_args(eleven)

    dialogue = sub.add_parser("dialogue")
    dialogue.add_argument("--text")
    dialogue.add_argument("--text-file")
    dialogue.add_argument("--speakers")
    dialogue.add_argument("--speakers-file")
    dialogue.add_argument("--delay", type=float, default=0)
    dialogue.add_argument("--with-transcript", action="store_true")
    dialogue.add_argument("--context-chaining", action="store_true")
    dialogue.add_argument("--file-name")
    dialogue.add_argument("--receive-url")
    dialogue.add_argument("--pronunciation-dictionary-id", type=int)
    add_common_wait_flags(dialogue)
    dialogue.set_defaults(func=cmd_dialogue)

    clone = sub.add_parser("voice-clone")
    clone.add_argument("--voice-name", required=True)
    clone.add_argument("--audio-file", required=True)
    clone.set_defaults(func=cmd_voice_clone)

    clone_delete = sub.add_parser("voice-clone-delete")
    clone_delete.add_argument("voice_clone_id")
    clone_delete.set_defaults(func=cmd_voice_clone_delete)

    dict_list = sub.add_parser("dictionary-list")
    dict_list.set_defaults(func=cmd_dictionary_list)

    dict_get = sub.add_parser("dictionary-get")
    dict_get.add_argument("dictionary_id")
    dict_get.set_defaults(func=cmd_dictionary_get)

    dict_create = sub.add_parser("dictionary-create")
    dict_create.add_argument("--name", required=True)
    dict_create.add_argument("--rules")
    dict_create.add_argument("--rules-file")
    dict_create.set_defaults(func=cmd_dictionary_create)

    dict_update = sub.add_parser("dictionary-update")
    dict_update.add_argument("dictionary_id")
    dict_update.add_argument("--name")
    dict_update.add_argument("--rules")
    dict_update.add_argument("--rules-file")
    dict_update.set_defaults(func=cmd_dictionary_update)

    dict_delete = sub.add_parser("dictionary-delete")
    dict_delete.add_argument("dictionary_id")
    dict_delete.set_defaults(func=cmd_dictionary_delete)

    dict_preview = sub.add_parser("dictionary-preview")
    dict_preview.add_argument("--text")
    dict_preview.add_argument("--text-file")
    dict_preview.add_argument("--rules")
    dict_preview.add_argument("--rules-file")
    dict_preview.set_defaults(func=cmd_dictionary_preview)

    sfx = sub.add_parser("sound-effect")
    sfx.add_argument("--text")
    sfx.add_argument("--text-file")
    sfx.add_argument("--duration-seconds", type=float)
    sfx.add_argument("--prompt-influence", type=float, default=0.3)
    sfx.add_argument("--loop", action="store_true")
    sfx.add_argument("--model-id", default="eleven_text_to_sound_v2")
    sfx.add_argument("--receive-url")
    add_common_wait_flags(sfx)
    sfx.set_defaults(func=cmd_sound_effect)

    poll = sub.add_parser("poll")
    poll.add_argument("task_id")
    poll.add_argument("--download", action="store_true")
    poll.add_argument("--out-dir")
    poll.add_argument("--interval", type=float, default=5)
    poll.add_argument("--timeout", type=float, default=900)
    poll.set_defaults(func=cmd_poll)

    tasks = sub.add_parser("list-tasks")
    tasks.add_argument("--page", type=int, default=1)
    tasks.add_argument("--limit", type=int, default=20)
    tasks.add_argument("--type")
    tasks.set_defaults(func=cmd_list_tasks)

    delete_tasks = sub.add_parser("delete-tasks")
    delete_tasks.add_argument("task_ids", nargs="+")
    delete_tasks.set_defaults(func=cmd_delete_tasks)

    return parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.func(args) or 0)


if __name__ == "__main__":
    raise SystemExit(main())
