# Zeus Recon — Architecture & Risk Mapping (GenLayer Intelligent Contracts)

> Phase 0 of the Zeus audit pipeline. Runs after Preflight.

## Goal
Map the Python codebase, identify all GenLayer interactions, and generate a ranked File Risk Table.

## Step 1: Entry Point Identification

Find all `.py` files containing classes that inherit from `gl.Contract`.
For each contract class, list:
- All `@gl.public.write` methods (state-modifying, externally callable).
- All `@gl.public.view` methods (read-only, externally callable).
- The `__init__` constructor and what storage it initializes.

## Step 2: Non-Deterministic Interaction Map

For each contract, catalog:
- Every `gl.nondet.exec_prompt()` call — note the prompt template and whether user input is concatenated.
- Every `gl.nondet.web.get()` / `gl.nondet.web.render()` call — note the URL source (hardcoded vs user-supplied).
- Every `gl.eq_principle.*` usage — which equivalence method wraps each nondet block.
- Every `gl.vm.run_nondet_unsafe()` call — examine the `leader_fn` and `validator_fn`.

## Step 3: Storage & Cross-Contract Map

For each contract, catalog:
- All persistent storage fields (type-annotated class attributes): `TreeMap`, `DynArray`, `u256`, `str`, `bool`, `Address`.
- All cross-contract calls via `gl.get_contract_at()` and `.emit()` / `.emit_transfer()`.
- Whether `gl.message.sender_address` or `gl.message.value` is checked in write methods.

## Step 4: File Risk Scoring

Score every `.py` file from 0-10 based on verified GenLayer heuristics:
- **+3** if it calls `gl.nondet.exec_prompt()` with any dynamic (non-literal) variable in the prompt string.
- **+3** if it calls `gl.nondet.web.get()` or `gl.nondet.web.render()` with a user-supplied URL.
- **+2** if it uses `gl.vm.run_nondet_unsafe()` (custom consensus = custom risk).
- **+1** if it calls `gl.get_contract_at()` and `.emit()` (cross-contract interaction).
- **+1** if it uses `u256` arithmetic without explicit underflow/overflow guards.

## Step 5: Module Selection

Based on the risk table, decide which Zeus detection lenses to activate in Phase 1:
- **Prompt Injection lens** → if any `gl.nondet.exec_prompt()` with dynamic input exists.
- **SSRF / Web Data lens** → if any `gl.nondet.web.*` with user-controlled URL exists.
- **Consensus Abuse lens** → if any `gl.vm.run_nondet_unsafe()` or complex equivalence logic exists.
- **Storage / Access Control lens** → always active.

## Output

Create `.audit/recon.md` containing:
1. Architecture summary (brief overview of what the contract does).
2. File Risk Table (sorted highest risk first).
3. Non-deterministic interaction inventory.
4. Storage field inventory.
5. Activated detection modules for Phase 1.
