---
name: zeus
description: AI-first security auditor for GenLayer Intelligent Contracts. 4-phase pipeline (recon → detection → state analysis → verification) with 12 heuristics across 4 detection lenses, 6 kill gates, and structured methodology audit trail per finding. Targets prompt injection, SSRF, consensus abuse, and storage bugs in gl.Contract Python code.
---

# Zeus — AI Security Auditor for GenLayer

Zeus is a structured audit methodology for GenLayer Intelligent Contracts, encoded as agent skills. It runs a 4-phase pipeline with multi-lens analysis and strict verification gates, specifically tuned for LLM integration (`gl.nondet.exec_prompt`), web connectivity (`gl.nondet.web.get`), the Equivalence Principle (`gl.eq_principle.*`), and Optimistic Democracy consensus.

## How It Works

When invoked via `/zeus`, a preflight readiness check runs first, then the pipeline runs sequentially:

- **Preflight** (`preflight/instructions.md`): Verifies `.py` files exist, `from genlayer import *` is present, and at least one `gl.Contract` subclass is defined.
1. **Phase 0 — Recon** (`recon/instructions.md`): Maps `gl.Contract` classes, catalogs all `gl.nondet.*` and `gl.eq_principle.*` calls, scores files by risk.
2. **Phase 1 — Detection** (`detector/instructions.md`): 4 parallel lenses (Prompt Injection, Web/SSRF, Equivalence/Consensus, State/Storage) with 12 heuristic checks.
3. **Phase 2 — State Analysis** (`state-auditor/instructions.md`): Storage field audit, hallucination impact matrix, `TreeMap`/`DynArray`/`u256` type verification, cross-contract `emit()` ordering.
4. **Phase 3 — Verification** (`critic/instructions.md`): 6 kill gates (Equivalence Guard, Prompt Structure, URL Restriction, GenVM Sandbox, Storage Persistence, Financial Impact).
5. **Phase 3b — Review** (`reviewer/instructions.md`): Devil's advocate on killed findings.
6. **Phase 4 — Report** (`reporter/instructions.md`): Structured markdown report with PoC traces and mitigations.

## Reference Files

### Phase Instructions
- `preflight/instructions.md` — GenLayer project readiness check
- `recon/instructions.md` — Architecture mapping and risk scoring
- `detector/instructions.md` — 4-lens detection with 12 heuristics (AI-01..03, WEB-01..02, EQ-01..03, ST-01..03, MSG-01)
- `state-auditor/instructions.md` — Storage and hallucination impact analysis
- `critic/instructions.md` — 6 kill gates
- `reviewer/instructions.md` — Second opinion on killed findings
- `reporter/instructions.md` — Final report generation
- `fuzzer/SKILL.md` — Property-based fuzz testing with LLM/web mocking

## Commands

| Command | Description |
|---------|-------------|
| `/zeus` | Full 4-phase GenLayer audit (auto-runs preflight first) |
| `/zeus-quick` | Skip state analysis for speed |
| `/zeus-review` | Second opinion on killed findings |
| `/zeus-fuzz` | Generate property-based fuzz tests for contract invariants |
| `/zeus-init` | Standalone readiness report (preflight only) |

Built by Wizbisy(https://github.com/Wizbisy).
