# Changelog

## [1.0.0] - 2026-07-20

### Added
- Complete 4-phase audit pipeline adapted for GenLayer Intelligent Contracts
- Preflight readiness check (`from genlayer import *`, `gl.Contract`, `Depends` comment)
- Recon phase with GenLayer-specific file risk scoring (`gl.nondet.*`, `gl.eq_principle.*`)
- Detection phase with 4 parallel lenses:
  - Lens A: Prompt Injection & LLM Output Safety
  - Lens B: Web Data & SSRF
  - Lens C: Equivalence Principle & Consensus Logic
  - Lens D: State, Storage & Access Control
- 12 heuristic checks: AI-01→03, WEB-01→02, EQ-01→03, ST-01→03, MSG-01
- State Analysis phase with hallucination impact matrix and storage type verification
- Critic phase with 6 kill gates (Equivalence, Prompt, URL, Sandbox, Storage, Impact)
- Reviewer phase for second opinion on killed findings
- Reporter phase with structured markdown output and PoC traces
- Fuzzer for property-based testing with LLM/web mocking
- 5 slash commands: `/zeus`, `/zeus-quick`, `/zeus-review`, `/zeus-fuzz`, `/zeus-init`
- Multi-marketplace support: `.claude-plugin`, `.codex-plugin`, `.agents`, `.kiro`
- Baseline test scenarios for 4 contract patterns
