# Contributing to Zeus

First off, thanks for taking the time to contribute! Zeus is an open-source security tool, and we welcome contributions that add new heuristics, improve the kill gates, or enhance GenLayer compatibility.

## How the Repository is Structured

Zeus acts as a standard agent plugin. The core logic lives in `skills/zeus/`:
- `SKILL.md`: The main entry point and metadata.
- `detector/instructions.md`: Contains the actual detection lenses and the heuristics.
- `critic/instructions.md`: Contains the kill gates.
- `tests/baseline-scenarios.md`: Contains the expected behavior of the agent.

## Making Changes

1. **Fork and clone** the repository.
2. **Make your changes**: 
   - If you are adding a new vulnerability check, add it to `skills/zeus/detector/instructions.md` and make sure to update the heuristic count.
   - If you are adding a new false-positive filter, add it to `skills/zeus/critic/instructions.md`.
3. **Regenerate the POWER.md file**: If you change `SKILL.md`, you MUST regenerate the `POWER.md` file so Kiro and other platforms stay in sync. Run this command from the root of the repository:
   ```bash
   python3 .github/scripts/build_power.py skills/zeus
   ```
4. **Test your changes**: We use an LLM-based testing approach. Please run your modified skill against the scenarios in `tests/baseline-scenarios.md` to ensure that it detects what it is supposed to detect and that the Critic properly filters out false positives.

## Pull Request Process

1. Ensure your PR description clearly describes the problem and solution.
2. If you added a new heuristic, please include a small code snippet in your PR showing a vulnerable GenLayer contract that your new heuristic successfully detects.
3. Keep PRs small and focused on one specific issue or heuristic.

## Code of Conduct

Please be respectful and constructive in all issues and pull requests. We are all here to make GenLayer Intelligent Contracts safer for everyone!
