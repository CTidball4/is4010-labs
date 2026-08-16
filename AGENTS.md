# AGENTS.md — IS4010 labs

This public repository contains 14 student labs for IS4010. Weeks 01–08 use the Python environment, and Weeks 09–14 use Rust.

## Scope of student edits

Students may edit only the deliverables named by the current lab:

- Week 01: `week01/student_setup.md`
- Week 02: `week02/lab02.py` and `week02/lab02_prompts.md`
- Weeks 03–08: the Python implementation files named in each `labXX.md`
- Weeks 09–14: implementation files under the corresponding `weekXX/src/`

Students and AI assistants must not modify:

- `README.md`, `AGENTS.md`, or any `labXX.md`
- `requirements.txt`, `Cargo.toml`, or `Cargo.lock`
- Anything under `.github/`
- Any `tests/` directory or embedded test module

## Grading contract

Each lab has one GitHub Actions workflow and one README badge. A green badge on the student's `main` branch means the complete lab earns 10 points. Tests must therefore cover every required deliverable without live network calls, API keys, or other secrets.

## Commands

Python example:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=week03 pytest week03/tests/ -v
```

Rust example:

```bash
cd week09
cargo test
cargo fmt --check
cargo clippy -- -D warnings
```

## Security

Never commit API keys, tokens, local configuration, virtual environments, build outputs, or instructor solutions. `week08/config.py` is intentionally ignored.
