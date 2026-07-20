# Pull Request

## Description

**Type of change:**
- [ ] New heuristic (detector lens)
- [ ] New kill gate (critic)
- [ ] Fix (correcting a false positive or detection failure)
- [ ] Refactor (reorganizing or improving clarity)
- [ ] Documentation (README, CONTRIBUTING)
- [ ] CI / tooling

**Summary:**
<!-- What does this change do and why? -->

## Testing Evidence (REQUIRED for heuristic/kill gate changes)

### Baseline Behavior (WITHOUT changes)

```text
Prompt: [test prompt on vulnerable contract]
Agent response: [verbatim or screenshot]
Issues: [why the current pipeline missed it or flagged a false positive]
```

### Target Behavior (WITH changes)

```text
Prompt: [same test prompt]
Agent response: [verbatim or screenshot]
Improvements: [how the new heuristic/gate fixed the issue]
```

- [ ] Ran the tests in `tests/baseline-scenarios.md` (plugin OFF then ON)
- [ ] Every scenario meets its `### Success Criteria`; no scenario fails
- [ ] Added/updated a scenario for any new or changed behavior

## Standards Compliance Checklist

### General

- [ ] Included a code snippet of a GenLayer contract demonstrating the vulnerability/false positive.
- [ ] `POWER.md` regenerated using `python3 .github/scripts/build_power.py skills/zeus` (if `SKILL.md` was modified).

### Content Quality

- [ ] `SKILL.md` remains lean. Detailed heuristics live in `detector/instructions.md`.
- [ ] Heuristic numbering is consistent (e.g., AI-04, WEB-03) and total count is updated.
- [ ] Code examples are accurate for GenVM (`TreeMap`, `gl.nondet.*`, etc.).
