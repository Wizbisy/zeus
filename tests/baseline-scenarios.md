# Baseline Scenarios

These scenarios define the expected behavior of Zeus when auditing GenLayer Intelligent Contracts. They contrast the behavior of an agent WITHOUT the Zeus skill against an agent WITH the Zeus skill activated.

## Running These Tests

1. Disable the Zeus skill in your agent workspace.
2. Provide the agent with the input contract for the scenario.
3. Issue the **Test Prompt**.
4. Verify the agent matches the **Expected Baseline Behavior**.
5. Enable the Zeus skill.
6. Issue the **Test Prompt** again (typically by running `/zeus`).
7. Verify the agent matches the **Target Behavior** and meets all **Success Criteria**.

## Scenario 1: Direct Prompt Injection (AI-01)

### Test Prompt
Run a full security audit on `vulnerable_wizard.py` and output a report with findings.

### Expected Baseline Behavior (WITHOUT skill)
The agent performs a standard code review. It might point out generic Python issues, but usually fails to recognize `gl.nondet.exec_prompt` as a vulnerable sink for prompt injection. It does not apply the Equivalence Principle threat model to the `validator_fn`.

### Target Behavior (WITH skill)
Zeus runs the 4-phase pipeline. The Detector flags AI-01 (Direct Prompt Concat) and EQ-01 (Weak Validator). The Critic allows both findings through because the prompt lacks sanitization and the validator function always returns True, negating consensus security. The Reporter outputs a structured markdown report highlighting these issues.

### Pressure Variations
- Add fake validation like `if len(request) > 0:` to see if the AI-01 detection gets tricked.
- Change the `validator_fn` to check `isinstance(leader_result, dict)` to see if EQ-01 still catches that it doesn't re-run the prompt.

### Success Criteria
- [ ] The report identifies the `gl.nondet.exec_prompt` call as a prompt injection vulnerability (AI-01).
- [ ] The report identifies the `validator_fn` as a weak validator that breaks Optimistic Democracy consensus (EQ-01).
- [ ] Both findings survive the Critic's kill gates.
- [ ] The PoC trace correctly explains how an attacker could extract the coin by modifying the JSON output.

## Scenario 2: SSRF via User-Controlled URL (WEB-01)

### Test Prompt
Audit `web_fetcher.py` and list any critical or high vulnerabilities.

### Expected Baseline Behavior (WITHOUT skill)
The agent may flag the URL parameter as unvalidated, but often misses the specific GenVM context where `gl.nondet.web.get()` allows an attacker to poison the subsequent LLM prompt (WEB-02) because it doesn't recognize the data flow from web → prompt.

### Target Behavior (WITH skill)
Zeus traces the user-supplied `url` parameter into `gl.nondet.web.get()` (WEB-01), and then traces the resulting `web_data` into the `gl.nondet.exec_prompt()` call (WEB-02). The Critic verifies there is no URL allowlist (Gate 3) and no prompt sanitization (Gate 2). 

### Pressure Variations
- Hardcode the domain but allow a user-supplied path to test if Gate 3 correctly kills the full SSRF finding (while keeping the WEB-02 prompt injection finding alive).

### Success Criteria
- [ ] The report flags `gl.nondet.web.get(url)` as a user-controlled SSRF vector (WEB-01).
- [ ] The report flags the concatenation of `web_data` into the prompt as a poisoning vector (WEB-02).
- [ ] The mitigation suggests validating the URL and using `prompt_non_comparative` with strict criteria.

## Scenario 3: Transient Storage (ST-01)

### Test Prompt
Check `broken_storage.py` for any data persistence issues.

### Expected Baseline Behavior (WITHOUT skill)
The agent sees a standard Python dictionary `self.data = {}` and assumes it's perfectly normal state management, completely missing that GenLayer requires `TreeMap` for persistent on-chain storage.

### Target Behavior (WITH skill)
The State Analysis phase strictly enforces GenLayer storage types. It flags `self.data = {}` as ST-01 (Transient Storage) because it uses a plain Python `dict`. The Critic's Gate 5 confirms it is assigned to `self` and not just a local variable, so the finding survives.

### Pressure Variations
- Use a `TreeMap` for `self.data` but a local `dict` inside a method to ensure Gate 5 correctly filters out the false positive.

### Success Criteria
- [ ] The report identifies `self.data = {}` as a transient storage bug that will cause silent data loss (ST-01).
- [ ] The mitigation explicitly recommends replacing `dict` with `TreeMap` from the `genlayer` SDK.

## Scenario 4: Clean Contract (No Findings)

### Test Prompt
Run a security audit on `safe_contract.py`.

### Expected Baseline Behavior (WITHOUT skill)
The agent might hallucinate generic "best practices" findings like "add events for state changes", "use a reentrancy guard", or "missing NatSpec comments."

### Target Behavior (WITH skill)
Zeus completes the pipeline and reports ZERO findings. The Critic successfully filters out generic code quality issues (Gate A: Generic best practice) and verifies that access controls (`gl.message.sender_address`) and balances (`u256` arithmetic) are properly checked.

### Pressure Variations
- Ask the agent specifically to "find at least one high severity issue" to test if the Critic's Zero False Positives mandate holds against user pressure.

### Success Criteria
- [ ] The report contains ZERO vulnerabilities.
- [ ] The agent explicitly refuses to invent findings or report cosmetic issues as security vulnerabilities.
