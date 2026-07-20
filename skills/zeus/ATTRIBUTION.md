# Attribution

Zeus's audit pipeline architecture is adapted from Krait, a Solidity smart contract auditor originally built by Zealynx Security. The pipeline structure (recon → detect → state analysis → verify → report) and the kill gate methodology were used as the foundation and then completely rewritten for GenLayer Intelligent Contracts.

## What's Original to Zeus

- Complete adaptation of the audit pipeline for GenLayer Intelligent Contracts (`gl.Contract`, `gl.nondet.*`, `gl.eq_principle.*`)
- 12 GenLayer-specific heuristics (AI-01→03, WEB-01→02, EQ-01→03, ST-01→03, MSG-01)
- 6 kill gates tuned for GenVM: Equivalence Guard, Prompt Structure, URL Restriction, GenVM Sandbox, Storage Persistence, Financial Impact
- Prompt Injection and SSRF detection lenses for `gl.nondet.exec_prompt()` and `gl.nondet.web.get()`
- Hallucination impact matrix for LLM-sourced state mutations
- `TreeMap`/`DynArray`/`u256` storage type verification
- Cross-contract `emit()` ordering analysis
- Property-based fuzz testing with LLM/web mocking

Built by [Wizbisy](https://github.com/Wizbisy).
