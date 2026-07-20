---
name: Feature Request
about: Suggest a new heuristic, kill gate, or idea for Zeus
title: '[FEAT] '
labels: enhancement
---

**Is your feature request related to a specific vulnerability? Please describe.**
<!-- A clear and concise description of the threat model or bug class. E.g., "Attackers can bypass gl.eq_principle.strict_eq() by doing X..." -->

**Describe the solution you'd like**
<!-- A clear and concise description of the new heuristic (for the detector) or kill gate (for the critic) you want to add. -->

**Example Vulnerable GenLayer Contract**
<!-- Provide a small Python snippet using `gl.Contract` that demonstrates the vulnerability. -->
```python
@gl.public.write
def vulnerable_method(self, user_input: str):
    # Example logic
    pass
```

**Testing the Feature**
<!-- How can we test that this feature works? (What would a baseline scenario look like?) -->

**Additional context**
<!-- Add any other context or screenshots about the feature request here. -->
