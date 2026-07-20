# Zeus Init — Standalone Readiness Report

Run a standalone preflight readiness check without starting a full audit.

## Usage

```
/zeus-init               # Check current directory
/zeus-init contracts/    # Check specific directory
```

## Instructions

Read and follow `preflight/instructions.md` in **report mode**.

Run all checks and emit the full summary table:

| Check | Status | Details |
|-------|--------|---------|
| Python files found | ✅/❌ | [count] .py files |
| GenLayer imports | ✅/❌ | `from genlayer import *` found in [files] |
| gl.Contract subclass | ✅/❌ | [class names] |
| Depends comment | ✅/⚠️ | Runtime hash present/missing |
| Public methods | ✅/⚠️ | [count] @gl.public.write + @gl.public.view |
| Known issues file | ✅/— | .audit/known-issues.md found/not found |

**Verdict**: `READY` / `READY (warnings)` / `NOT READY`

**CRITICAL:**
- Read-only. Do NOT modify any files unless the user explicitly says "fix it."
- If verdict is `READY`, suggest `/zeus` next.
- If verdict is `NOT READY`, explain what needs to be fixed first.
