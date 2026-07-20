# Zeus Quick — Fast Audit (Skip State Analysis)

Run a faster audit that skips Phase 2 (State Analysis) for speed.

## Usage

```
/zeus-quick              # Quick audit current directory
/zeus-quick contracts/   # Quick audit specific directory
```

## Instructions

Run the same pipeline as `/zeus` but skip Phase 2 (State Analysis):

1. **Preflight** → Check for GenLayer project structure
2. **Phase 0 — Recon** → Architecture mapping and file risk scoring
3. **Phase 1 — Detection** → 4-lens analysis with 12 heuristics
4. ~~Phase 2 — State Analysis~~ → **SKIPPED**
5. **Phase 3 — Verification** → 6 kill gates
6. **Phase 4 — Report** → Final output

This is useful for quick first-pass reviews or smaller contracts where state analysis adds little value.

**Note:** Skipping State Analysis means hallucination impact, storage type verification, and cross-contract emit ordering checks will NOT be performed. For a thorough audit, use `/zeus` instead.
