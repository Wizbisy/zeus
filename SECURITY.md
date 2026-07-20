# Security Policy

## Supported Versions

Currently, only the latest release of Zeus on the `main` branch is actively supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| >= 1.0  | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Zeus is a security auditing tool, which means its own security and integrity are paramount. If you discover a vulnerability *in Zeus itself* (for example, a prompt injection payload that can bypass the Critic gates, or a flaw in the `build_power.py` script), please do **not** open a public issue.

Instead, please email the maintainer directly at **wizbisy@gmail.com** (or reach out via direct message if an email is not available).

Please include:
- A description of the vulnerability.
- A proof of concept (PoC) or steps to reproduce the issue (e.g., a vulnerable GenLayer contract that successfully bypasses the detection pipeline).
- Any potential mitigation strategies you suggest.

You can expect an initial acknowledgment within 48 hours. We take all reports seriously and will work with you to patch the vulnerability and credit you in the ensuing release.
