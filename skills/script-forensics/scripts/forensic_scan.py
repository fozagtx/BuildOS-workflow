#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


CONTRAST_PATTERNS = [
    r"\bnot\s+just\b",
    r"\bnot\s+only\b",
    r"\bnot\s+merely\b",
    r"\bmore\s+than\s+just\b",
    r"\bit'?s\s+not\s+about\b",
    r"\bit\s+is\s+not\s+about\b",
    r"\bthis\s+is\s+not\b",
    r"\bit\s+is\s+not\b",
    r"\bnot\s+because\b",
]


def normalize_words(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9']+", text.lower())


def split_sentences(text: str) -> list[str]:
    chunks = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def ngrams(words: list[str], n: int) -> Counter[tuple[str, ...]]:
    return Counter(tuple(words[i : i + n]) for i in range(max(0, len(words) - n + 1)))


def sentence_starts(sentences: list[str], words: int) -> Counter[str]:
    starts: Counter[str] = Counter()
    for sentence in sentences:
        tokens = normalize_words(sentence)
        if len(tokens) >= words:
            starts[" ".join(tokens[:words])] += 1
    return starts


def find_contrast_lines(text: str) -> list[tuple[int, str, str]]:
    findings: list[tuple[int, str, str]] = []
    lines = text.splitlines()
    compiled = [(pattern, re.compile(pattern, re.IGNORECASE)) for pattern in CONTRAST_PATTERNS]
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        for pattern, regex in compiled:
            if regex.search(stripped):
                findings.append((idx, pattern, stripped))
                break
    return findings


def print_counter(title: str, counter: Counter, limit: int) -> None:
    items = [(key, count) for key, count in counter.most_common() if count > 1]
    print(f"\n{title}")
    if not items:
        print("- none")
        return
    for key, count in items[:limit]:
        if isinstance(key, tuple):
            key = " ".join(key)
        print(f"- {count}x: {key}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Find repeated phrases and AI-slop contrast patterns in scripts.")
    parser.add_argument("script", type=Path)
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--ngram-min", type=int, default=4)
    parser.add_argument("--ngram-max", type=int, default=8)
    args = parser.parse_args()

    text = args.script.read_text(encoding="utf-8")
    words = normalize_words(text)
    sentences = split_sentences(text)

    print(f"Script: {args.script}")
    print(f"Words: {len(words)}")
    print(f"Sentences: {len(sentences)}")

    contrast = find_contrast_lines(text)
    print("\nAI-slop contrast patterns")
    if not contrast:
        print("- none")
    else:
        for line_no, pattern, line in contrast[: args.limit]:
            print(f"- line {line_no}, pattern {pattern}: {line}")

    print_counter("Repeated sentence starts, first 3 words", sentence_starts(sentences, 3), args.limit)
    print_counter("Repeated sentence starts, first 4 words", sentence_starts(sentences, 4), args.limit)

    for n in range(args.ngram_min, args.ngram_max + 1):
        repeated = Counter({key: value for key, value in ngrams(words, n).items() if value > 1})
        print_counter(f"Repeated {n}-word phrases", repeated, args.limit)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
