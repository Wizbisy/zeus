# Zeus Preflight — Readiness Check (GenLayer Intelligent Contracts)

> Step 0 of the Zeus audit pipeline. Must pass before Recon begins.

## Goal
Verify that the workspace contains valid GenLayer Intelligent Contract code.

## Checklist

### 1. Python File Check
- Look for `.py` files in the project directory.
- **Failure:** If no `.py` files exist, this is not a GenLayer project. ABORT.

### 2. GenLayer Import Check
- Verify that at least one `.py` file contains `from genlayer import *`.
- Check for the `Depends` magic comment on the first line: `# { "Depends": "py-genlayer:..." }`.
- **Failure:** If no GenLayer imports are found, ABORT with a message explaining this tool audits GenLayer Intelligent Contracts specifically.

### 3. Contract Class Check
- Verify that at least one class inherits from `gl.Contract`.
- **Failure:** If no `gl.Contract` subclass exists, ABORT.

### 4. Decorator Check
- Verify that at least one method uses `@gl.public.write` or `@gl.public.view`.
- **Warning (non-blocking):** If no public methods exist, the contract has no external interface — flag this but continue.

### 5. Known Issues Check
- Look for a `.audit/known-issues.md` file. If it exists, load it so the Detector can skip already-acknowledged issues.

## Output

If all checks pass:
```
PREFLIGHT SUCCESS: Workspace contains valid GenLayer Intelligent Contract code.
- Files found: [count] .py files
- Contracts found: [list of class names]
- GenVM runtime: [Depends hash]
Proceeding to Phase 0 (Recon)...
```
