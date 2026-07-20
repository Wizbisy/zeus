# Zeus Reviewer — Second Opinion (GenLayer Intelligent Contracts)

> Invoked by `/zeus-review`. Independent re-evaluation of killed findings.

## Purpose
Double-check findings that were killed by the Critic. Play Devil's Advocate.

## For Each Killed Finding

### 1. Re-examine the Kill Gate that killed it.

**If killed by Gate 1 (Equivalence):**
- Is the `validator_fn` in `gl.vm.run_nondet_unsafe()` actually robust? Does it re-execute the prompt, or does it just check the type?
- Could an attacker craft input that causes BOTH the leader and validator LLMs to agree on a malicious output (e.g., both GPT-4 and LLaMA would interpret the prompt injection the same way)?

**If killed by Gate 2 (Prompt Structure):**
- Is the sanitization actually effective? Does it handle Unicode tricks, base64 encoding, or multi-line injection?
- Can the attacker bypass `response_format="json"` by embedding instructions in a JSON value string?

**If killed by Gate 3 (URL Restriction):**
- Is the URL allowlist comprehensive? Could an attacker use URL encoding, redirects, or DNS rebinding?
- Even if the URL is restricted, is the response content validated before being used?

**If killed by Gate 4 (Sandbox):**
- Are there any dynamic import patterns (`__import__`, `importlib`) that could bypass GenVM restrictions?
- Does the WASM sandbox have any known escape vectors for the specific Wasmtime version?

**If killed by Gate 5 (Storage):**
- Is the `dict`/`list` truly local? Or is it assigned to `self.*` via an indirect reference?

**If killed by Gate 6 (Impact):**
- Could the "minor" issue be chained with another finding to escalate impact?
- Could repeated exploitation drain gas via appeal cycles?

### 2. Verdict
If the Reviewer finds a valid counter-argument to the Kill Gate, **RESURRECT** the finding and pass it to the Reporter with an explanation of why the Kill Gate was wrong.

If not, confirm the kill.
