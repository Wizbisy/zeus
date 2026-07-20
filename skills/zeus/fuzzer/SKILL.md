# Zeus Fuzzer — Property-Based Testing (GenLayer Intelligent Contracts)

> Triggered by `/zeus-fuzz`.

## Goal
Generate property-based fuzz tests for GenLayer Intelligent Contracts.

## Approach

Since GenLayer contracts run inside GenVM (a WASM sandbox), traditional Foundry fuzzing does not apply. Instead, Zeus generates Python test scripts that:

1. **Identify state invariants** from the contract code. Examples:
   - "Total supply must always equal the sum of all `balances` values in the `TreeMap`."
   - "`self.has_coin` can only transition from `True` to `False`, never back."
   - "Only the owner address can call `withdraw()`."

2. **Simulate LLM hallucinations** by mocking `gl.nondet.exec_prompt()` responses:
   - Return malformed JSON instead of valid `response_format="json"`.
   - Return unexpected types (string instead of bool, null instead of dict).
   - Return adversarial prompt injection payloads as the "LLM response."

3. **Simulate web failures** by mocking `gl.nondet.web.get()` responses:
   - Return empty strings, massive payloads, or HTML containing adversarial text.
   - Simulate timeout/connection errors.

4. **Verify invariants hold** after each simulated call.

## Output

Generate a `test_zeus_fuzz.py` file containing:
- Mock classes for `gl.nondet.exec_prompt()` and `gl.nondet.web.get()`.
- Property tests for each identified invariant.
- Edge case inputs derived from the heuristic findings.

Note: These tests are designed to run OUTSIDE GenVM (as standard Python unit tests) to validate contract logic against adversarial inputs.
