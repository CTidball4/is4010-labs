# Lab 05: Functions and error handling

**Due:** Sunday at 11:59 PM  
**Points:** 10

Refactor data-processing logic into small functions that handle missing and invalid values gracefully.

## Deliverable

Create `week05/lab05.py`. Do not copy or modify the provided tests.

## Functions

```python
def calculate_average_age(users):
    """Return the average numeric age, or 0.0 when none are valid."""


def get_active_user_emails(users):
    """Return email addresses belonging to active users."""
```

Requirements:

- A user is represented by a dictionary.
- Ignore missing ages and ages that are not numeric.
- Return `0.0` when there are no valid ages.
- Include an email only when `is_active` is truthy and the email key exists.
- Return an empty list when no active email addresses exist.
- Include clear docstrings.

## Test locally

```bash
uv run --directory week05 python -m pytest tests/ -v
```

## If a test fails

`pytest` prints the failing test's name, the line that failed, and the expected and actual
values. That is enough context for a coding agent to diagnose it: paste the full output into
Copilot CLI, Antigravity CLI, or a browser chat and ask what behavior the test expects and why
yours differs.

Ask for an explanation, not just a passing grade. You are responsible for every line you submit,
so make sure you can explain the fix before you commit it.

## Submit

```bash
git add week05/lab05.py
git commit -m "Complete Lab 05"
git push origin main
```

A green Week 05 badge earns 10 points.
