#!/usr/bin/env node
/**
 * Validate ROUTE_REGISTRY.json paths exist under skill/sources/
 * Usage: node scripts/validate-routes.mjs
 */
import { readFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");
const registryPath = join(root, "skill", "ROUTE_REGISTRY.json");
const stylePath = join(root, "skill", "STYLE_PRESETS.json");
const sourcesRoot = join(root, "skill", "sources");

if (!existsSync(registryPath)) {
  console.error("Missing", registryPath);
  process.exit(1);
}

const registry = JSON.parse(readFileSync(registryPath, "utf8"));
const missing = [];
const checked = new Set();

function check(rel) {
  if (!rel || checked.has(rel)) return;
  checked.add(rel);
  const full = join(sourcesRoot, rel);
  if (!existsSync(full)) missing.push(rel);
}

for (const surface of Object.values(registry.surfaces || {})) {
  for (const route of Object.values(surface.routes || {})) {
    for (const p of route.primary || []) check(p);
    for (const p of route.secondary || []) check(p);
  }
}
for (const p of Object.values(registry.field_router?.map || {})) check(p);

if (existsSync(stylePath)) {
  const style = JSON.parse(readFileSync(stylePath, "utf8"));
  for (const preset of Object.values(style.presets || {})) {
    for (const p of preset.must_read || []) check(p);
    for (const p of preset.optional_read || []) check(p);
  }
  console.log(`Style presets: ${Object.keys(style.presets || {}).join(", ")} (default ${style.default_preset})`);
} else {
  console.warn("STYLE_PRESETS.json missing — style axis not validated");
}

console.log(`Design ProMax route validation (registry v${registry.version})`);
console.log(`Checked ${checked.size} unique paths under skill/sources/`);

if (missing.length) {
  console.error("MISSING:");
  for (const m of missing) console.error("  -", m);
  process.exit(1);
}

console.log("OK — all registry + style paths exist.");
process.exit(0);
