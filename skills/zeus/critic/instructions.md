# Zeus Critic — Kill Gates (GenLayer Intelligent Contracts)

> Phase 3 of the Zeus audit pipeline. Runs after State Analysis.

## Purpose
The Critic is a hostile filter. Its sole job is to DESTROY findings from the Detector. If a finding cannot survive every Kill Gate, it is a False Positive and must be discarded.

## The 6 Kill Gates

Run every finding through ALL 6 gates. If ANY gate returns TRUE, **KILL THE FINDING**.

### Gate 1: Equivalence Principle Guard
- **Question:** Does the exploit rely on manipulating a non-deterministic output (LLM/web)?
- **Kill Condition:** The non-deterministic call is wrapped in `gl.eq_principle.strict_eq()`, `gl.eq_principle.prompt_non_comparative()`, or `gl.vm.run_nondet_unsafe()` with a robust `validator_fn` that independently verifies the output. The validator function re-executes the prompt and compares results — meaning a manipulated leader output would be rejected by the validator majority. **KILL IT.**

### Gate 2: Prompt Structure Gate
- **Question:** Does the Prompt Injection finding rely on user input reaching `gl.nondet.exec_prompt()`?
- **Kill Condition:** The user input is sanitized, XML-tagged, length-limited, or placed in a structured `response_format="json"` schema where the LLM cannot interpret injected instructions as commands. The prompt template uses strict delimiters that prevent breakout. **KILL IT.**

### Gate 3: URL Restriction Gate
- **Question:** Does the SSRF/WEB finding rely on a user-controlled URL reaching `gl.nondet.web.get()` or `gl.nondet.web.render()`?
- **Kill Condition:** The URL is constructed from a hardcoded domain with only a path segment from user input, or the URL is validated against an allowlist before being passed to the web API. The response is not used in any state mutation or LLM prompt. **KILL IT.**

### Gate 4: GenVM Sandbox Gate
- **Question:** Does the exploit assume standard Python capabilities (file I/O, network sockets, subprocess)?
- **Kill Condition:** GenVM runs in a WASM sandbox (Wasmtime). There is no `os`, `sys`, `subprocess`, `socket`, or filesystem access. The only external I/O available is through `gl.nondet.web.*` and `gl.nondet.exec_prompt()`. If the exploit requires anything outside these APIs, the GenVM sandbox will inherently block it. **KILL IT.**

### Gate 5: Storage Persistence Gate
- **Question:** Does the finding claim data loss from using `dict`/`list` instead of `TreeMap`/`DynArray`?
- **Kill Condition:** The `dict`/`list` is used as a LOCAL variable within a single method call (not assigned to `self.*`). Local variables don't need to persist — only class attributes do. If the transient collection is never assigned to persistent storage, there is no bug. **KILL IT.**

### Gate 6: Financial Impact Gate
- **Question:** Does this issue result in stolen funds, locked funds, bricked consensus, or permanent state corruption?
- **Kill Condition:** The issue is purely cosmetic, causes a temporary inconvenience (e.g., a single transaction reverts), or slightly degrades LLM accuracy without any state corruption, fund theft, or consensus failure. **KILL IT.**

## Output Format

For each finding:
```
Finding: [Title]
Gate 1 (Equivalence): SURVIVES / KILLED — [reason]
Gate 2 (Prompt):       SURVIVES / KILLED — [reason]
Gate 3 (URL):          SURVIVES / KILLED — [reason]
Gate 4 (Sandbox):      SURVIVES / KILLED — [reason]
Gate 5 (Storage):      SURVIVES / KILLED — [reason]
Gate 6 (Impact):       SURVIVES / KILLED — [reason]
VERDICT: SURVIVES / KILLED
```
