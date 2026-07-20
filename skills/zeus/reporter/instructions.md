# Zeus Reporter — Final Report (GenLayer Intelligent Contracts)

> Final phase. Formats surviving findings into a professional audit report.

## Output Format

For every surviving finding, output a structured report block:

### Finding Template

```markdown
## [SEVERITY] — [Title]

### Impact
How does this affect the contract's users, state, consensus, or funds?

### Vulnerability
The specific code pattern and why it is dangerous. Reference the actual GenLayer API involved:
- `gl.nondet.exec_prompt()` for prompt injection
- `gl.nondet.web.get()` / `gl.nondet.web.render()` for SSRF
- `gl.eq_principle.*` / `gl.vm.run_nondet_unsafe()` for consensus logic
- `TreeMap` / `DynArray` / `u256` for storage issues
- `gl.get_contract_at().emit()` for cross-contract issues
- `gl.message.sender_address` for access control

### Proof of Concept
A step-by-step attack trace:
1. Attacker calls `contract.method("malicious input")`
2. The input reaches `gl.nondet.exec_prompt(f"...{malicious_input}...")`
3. The LLM returns `{"give_coin": true}` due to prompt injection
4. The contract writes `self.has_coin = False` — coin is stolen

### Mitigation
Concrete fix for the Python code. Examples:
- "Sanitize user input before concatenating into prompts"
- "Use `gl.eq_principle.prompt_non_comparative()` with strict criteria instead of `strict_eq()`"
- "Add `if gl.message.sender_address != self.owner: raise gl.vm.UserError('unauthorized')`"
- "Replace `self.data = {}` with `self.data = TreeMap()`"
```

## Report Structure

Group findings by severity:
1. **Critical** — Funds at risk, state corruption, consensus manipulation.
2. **High** — Prompt injection, SSRF, access control bypass.
3. **Medium** — Weak validator functions, vague equivalence criteria, missing error handling.
4. **Low** — Informational, gas inefficiency, cosmetic issues.

End with a summary table:
| ID | Severity | Title | Status |
|---|---|---|---|
| AI-01 | High | Direct Prompt Concatenation in `ask_for_coin` | Confirmed |
| ... | ... | ... | ... |
