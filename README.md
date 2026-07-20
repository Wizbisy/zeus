# Zeus Auditor

[![Agent Skills](https://img.shields.io/badge/Agent-Skills-5865F2)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-marketplace-D97757)](https://code.claude.com/docs/en/plugins-reference)
[![Codex](https://img.shields.io/badge/Codex-marketplace-000000)](https://github.com/openai/codex)

Zeus is an AI-first security auditor specifically designed for **GenLayer Intelligent Contracts**. It runs a structured 4-phase audit pipeline to detect vulnerabilities unique to LLM integration, web connectivity, the Equivalence Principle, and the GenVM execution environment.

Executable discipline for AI coding agents - skills the agent loads on demand and applies while **it works**, not prose guides _it ignores_.

## Install

### npx skills - recommended for any Agent Skills host

Works with any compatible agent (Claude Code, Cursor, Copilot, Gemini CLI, OpenCode, Codex, and more). Each command is independent - run the one(s) you want:

```bash
npx skills add https://github.com/Wizbisy/zeus
```

### Claude Code

```bash
/plugin marketplace add Wizbisy/zeus
/plugin install zeus@Wizbisy
```

### Codex

```bash
codex plugin marketplace add Wizbisy/zeus
```

Then run `codex`, open `/plugins`, select **zeus**, and install it.

For other hosts, expand below.

<!-- prettier-ignore-start -->

<details>
<summary>Cursor</summary>

```bash
git clone https://github.com/Wizbisy/zeus.git
ln -s "$(pwd)/zeus/skills/zeus" ~/.cursor/skills/zeus
```

Cursor auto-discovers skills from `.agents/skills/` and `.cursor/skills/`.
</details>

<details>
<summary>Copilot</summary>

```bash
git clone https://github.com/Wizbisy/zeus.git ~/.copilot/skills/zeus
```

Copilot auto-discovers skills from `.copilot/skills/`.
</details>

<details>
<summary>OpenCode</summary>

```bash
git clone https://github.com/Wizbisy/zeus.git ~/.agents/skills/zeus
```

OpenCode auto-discovers skills from `.agents/skills/`, `.opencode/skills/`, and `.claude/skills/`.
</details>

<details>
<summary>Antigravity / Antigravity IDE</summary>

```bash
git clone https://github.com/Wizbisy/zeus.git
ln -s "$(pwd)/zeus/skills/zeus" ~/.gemini/config/skills/zeus
```

</details>

<details>
<summary>Kiro (Powers)</summary>

Zeus is also available as a [Kiro Power](https://kiro.dev/docs/powers/).
In Kiro: **Powers panel → "Add power from GitHub"**, then paste:

```text
https://github.com/Wizbisy/zeus
```
</details>

<!-- prettier-ignore-end -->

## What changes with the plugin

> Routes GenLayer audits to a rigorous 4-phase methodology instead of blind text-based guessing. Ensures GenVM and Equivalence Principle specifics are respected.

**tldr** - what changes with the plugin:

| Prompt | Without the plugin | With the plugin |
|--------|--------------------|-----------------|
| `/zeus` | Agent blindly guesses security issues with standard Python tools | Agent runs a rigorous 4-phase GenLayer audit pipeline with 12 GenVM-specific heuristics |
| `/zeus-fuzz` | Agent struggles to write GenLayer-compatible tests | Agent generates property-based fuzz tests mocking `gl.nondet.*` |
| `/zeus-review` | Agent accepts false positives | Agent critically evaluates killed findings through 6 kill gates |

Try:
- `/zeus`
- `/zeus-quick`
- `/zeus-fuzz`
- `/zeus-review`
- `/zeus-init`

## Features & Detection Lenses

- **GenLayer Native**: Specifically built for Python contracts using the `genlayer` SDK (`gl.Contract`, `gl.nondet.*`, `gl.eq_principle.*`).
- **4-Lens Detection**: Analyzes contracts for:
  - **Lens A (AI-01→03)**: Prompt Injection & LLM Output Safety
  - **Lens B (WEB-01→02)**: Web Data & SSRF
  - **Lens C (EQ-01→03)**: Equivalence Principle & Consensus Logic
  - **Lens D (ST-01→03, MSG-01)**: State, Storage & Access Control
- **State Auditor**: Tracks state mutations driven by non-deterministic outputs and verifies appropriate GenVM storage types (`TreeMap`, `DynArray`, `u256`).
- **Strict Verification (Critic)**: 6 kill gates automatically destroy false positives (e.g., verifying GenVM sandbox restrictions, URL allowlists, or `validator_fn` robustness) before they reach the final report.
- **Property-Based Fuzzing**: Auto-generates Python test scripts that mock non-deterministic LLM/web APIs with adversarial payloads to fuzz contract invariants.

## Why this plugin

- **Honest by construction.** Any findings killed by the 6 kill gates are logged and can be reviewed via `/zeus-review`, so you can trust what the agent reports.
- **Token-lean.** A short `SKILL.md` routes to reference files that load only when the task needs them. The agent does not carry the whole guide in context.
- **Portable.** One discipline across Claude Code, Cursor, Copilot, Antigravity, OpenCode, Codex, and Kiro.

## Authors & Attribution

Zeus is built by [Wizbisy](https://github.com/Wizbisy).

The pipeline architecture and verification methodology were adapted from Krait (by Zealynx Security). For full details, see [ATTRIBUTION.md](skills/zeus/ATTRIBUTION.md).

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
