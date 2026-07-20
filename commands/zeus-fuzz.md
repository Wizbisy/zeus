# Zeus Fuzz — Property-Based Fuzz Testing

Generate property-based fuzz tests for GenLayer Intelligent Contract invariants.

## Usage

```
/zeus-fuzz               # Generate fuzz tests for current project
/zeus-fuzz contracts/    # Generate for specific directory
```

## Instructions

Read and follow `fuzzer/SKILL.md`.

**Steps:**
1. Identify the target `gl.Contract` subclass(es).
2. Extract state invariants from the contract logic:
   - Balance conservation (sum of all values in a `TreeMap` must equal total supply)
   - State transition rules (e.g., `has_coin` can only go `True → False`)
   - Access control invariants (only owner can call certain methods)
3. Generate `test_zeus_fuzz.py` with:
   - Mock classes for `gl.nondet.exec_prompt()` and `gl.nondet.web.get()`
   - Adversarial LLM responses (malformed JSON, unexpected types, prompt injection payloads)
   - Adversarial web responses (empty, massive, adversarial text)
   - Property assertions for each invariant
4. Present the generated test file to the user.

**Note:** These tests run as standard Python unit tests OUTSIDE GenVM. They validate contract logic against adversarial inputs by mocking the non-deterministic APIs.

**Output:** `test_zeus_fuzz.py` in the project root.
