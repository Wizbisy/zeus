# Zeus State Auditor (GenLayer Intelligent Contracts)

> Phase 2 of the Zeus audit pipeline. Runs after Detection, before Critic.

## Purpose
Verify that ALL state mutations are authorized, validated, and resistant to hallucination corruption.

## Step 1: Storage Field Audit

For every persistent storage field declared on a `gl.Contract` subclass:
- **Field name and type** (e.g., `balances: TreeMap[Address, u256]`).
- **Which `@gl.public.write` methods mutate it.**
- **What is the source of the value being written?**
  - Direct user input → Medium risk.
  - LLM output from `gl.nondet.exec_prompt()` → High risk.
  - Web data from `gl.nondet.web.get()` → High risk.
  - Computed from existing state → Low risk.

## Step 2: Hallucination Impact Matrix

For every state mutation sourced from an LLM output:
| Question | Safe | Dangerous | Critical |
|---|---|---|---|
| What happens if the LLM returns garbage JSON? | Transaction reverts via `gl.vm.UserError` | Garbage is silently stored | Garbage overwrites another user's data |
| What happens if the LLM returns the wrong boolean? | No state change | Wrong branch taken, minor effect | Funds transferred to wrong address |
| What happens if the LLM ignores `response_format="json"`? | `try/except` catches the parse error | Contract crashes mid-state-update | Partial state written, storage corrupted |

## Step 3: Storage Type Verification

Check that persistent data uses the correct GenLayer storage types:
- `TreeMap[K, V]` for mappings (NOT Python `dict`).
- `DynArray[T]` for arrays (NOT Python `list`).
- `u256` / `i32` / `bigint` for integers (NOT Python `int` for storage fields).
- `Address` for account addresses.

If a `@gl.public.write` method assigns a plain `dict` or `list` to `self.*`, flag it as **ST-01: Transient Storage** (Critical — data will be silently lost on next transaction).

## Step 4: Access Control Audit

For every `@gl.public.write` method:
- Does it check `gl.message.sender_address` before performing privileged operations?
- Does it check `gl.message.value` before crediting balances?
- If there is an "owner" pattern, is the owner address stored in a persistent field set during `__init__`?

## Step 5: Cross-Contract State Ordering

For every `gl.get_contract_at().emit()` call:
- Is `self.*` state modified BEFORE or AFTER the `emit()`?
- If state is modified before `emit(on='finalized')` and the child transaction fails, is the parent state left in an inconsistent state?
- Check `on='accepted'` vs `on='finalized'` — if the parent transaction is overturned on appeal after an `on='accepted'` child fires, state may be inconsistent.

## Output

Produce a State Audit brief listing:
1. All storage fields and their mutation sources.
2. Hallucination impact assessment for each LLM-sourced mutation.
3. Storage type violations (ST-01 findings).
4. Access control gaps (ST-02 findings).
5. Cross-contract ordering concerns (MSG-01 findings).

Hand all findings to the Critic phase.
