#!/usr/bin/env python3
"""POWER.md generator for standalone plugins (Kiro Power)."""

import json
import os
import re
import sys

def parse_frontmatter(skill_path):
    src = open(skill_path, encoding="utf-8").read()
    if not src.startswith("---"):
        raise SystemExit(f"build_power: {skill_path} has no leading --- frontmatter")
    parts = src.split("---")
    fm, body = parts[1], "---".join(parts[2:])
    out = {}
    for raw in fm.splitlines():
        line = raw.rstrip("\r")
        m = re.match(r"^name:\s*(.+?)\s*$", line)
        if m: out["name"] = m.group(1); continue
        m = re.match(r"^description:\s*(.+?)\s*$", line)
        if m: out["description"] = m.group(1); continue
        m = re.match(r"^author:\s*(.+?)\s*$", line)
        if m: out["author"] = m.group(1); continue
        m = re.match(r"^version:\s*(.+?)\s*$", line)
        if m: out["version"] = m.group(1); continue
    for k in ("name", "description"):
        if not out.get(k):
            raise SystemExit(f"build_power: {skill_path} frontmatter missing {k}")
    return out, body

def yaml_dq(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def build_power(skill_dir):
    skill_dir = skill_dir.replace("\\", "/").rstrip("/")
    name = os.path.basename(skill_dir)
    skill_path = os.path.join(skill_dir, "SKILL.md")
    repo_root = os.getcwd()
    codex_path = os.path.join(repo_root, ".codex-plugin", "plugin.json")

    meta, body = parse_frontmatter(skill_path)

    if not os.path.isfile(codex_path):
        raise SystemExit(f"build_power: {codex_path} not found")
    codex = json.load(open(codex_path, encoding="utf-8"))
    display_name = (codex.get("interface") or {}).get("displayName") or meta["name"]
    keywords = codex.get("keywords") or []
    author = codex.get("author") or meta.get("author") or "Wizbisy"
    version = codex.get("version") or meta.get("version") or "1.0.0"

    rewritten = re.sub(r"\]\(references/", f"](skills/{name}/references/", body)
    rewritten = re.sub(r"^\n+", "", rewritten)
    rewritten = re.sub(r"\s*$", "", rewritten)

    front = "\n".join([
        "---",
        f"name: {yaml_dq(meta['name'])}",
        f"displayName: {yaml_dq(display_name)}",
        f"description: {yaml_dq(meta['description'])}",
        f"keywords: [{', '.join(yaml_dq(k) for k in keywords)}]",
        f"author: {yaml_dq(author)}",
        f"version: {version}",
        "---",
    ])

    banner = (
        "<!-- GENERATED FILE - DO NOT EDIT. Source: "
        f"{skill_path.replace(os.sep, '/')}. Regenerate: python3 .github/scripts/build_power.py "
        f"{skill_dir}. CI-owned (version sync), like "
        ".codex-plugin/plugin.json. -->"
    )

    doc = f"{front}\n\n{banner}\n\n{rewritten}\n"
    return doc, repo_root

def main(argv):
    args = [a for a in argv if a != "--check"]
    check = "--check" in argv
    if len(args) != 1:
        raise SystemExit("usage: build_power.py <skill_dir> [--check]")
    skill_dir = args[0]
    
    generated, repo_root = build_power(skill_dir)
    dest = os.path.join(repo_root, "POWER.md")
    current = open(dest, encoding="utf-8").read() if os.path.isfile(dest) else None

    if check:
        if current != generated:
            print(f"build_power: {dest} is out of sync with {skill_dir}/SKILL.md.")
            sys.exit(1)
        print(f"build_power: {dest} in sync")
        return
    if current == generated:
        print(f"build_power: {dest} already up to date")
        return
    with open(dest, "w", encoding="utf-8") as f:
        f.write(generated)
    print(f"build_power: wrote {dest}")

if __name__ == "__main__":
    main(sys.argv[1:])
