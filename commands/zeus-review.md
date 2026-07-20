# Zeus Review — Second Opinion on Killed Findings

Re-examine findings that were killed by the Critic to catch over-filtering.

## Usage

```
/zeus-review             # Review kills from most recent audit
```

## Instructions

Read and follow `reviewer/instructions.md`.

**Prerequisites:**
- `.audit/findings/critic-verdicts.md` must exist (from a previous `/zeus` run).
- Load all findings with verdict `KILLED`.

For each killed finding:
1. Identify which Kill Gate killed it (Equivalence, Prompt Structure, URL Restriction, GenVM Sandbox, Storage Persistence, or Financial Impact).
2. Play Devil's Advocate against that specific gate.
3. If a valid counter-argument exists, **RESURRECT** the finding.

**Output:**
- List of reviewed kills with verdict: `CONFIRMED KILL` or `RESURRECTED`.
- For resurrected findings, explain why the Kill Gate was wrong and pass to the Reporter.

This command is useful when you suspect the Critic was too aggressive and real bugs were filtered out.
