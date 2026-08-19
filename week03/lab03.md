# Lab 03: Python basics and automated testing

**Due:** Sunday at 11:59 PM  
**Points:** 10

This is the first lab in which you write Python directly. You will practice functions, strings, conditionals, loops, user input, and automated testing.

## Deliverable

Create `week03/lab03.py`. Do not modify the tests.

## Part 1: Mad Lib generator

Implement:

```python
def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
```

The result must be a string and must contain the adjective, noun, and verb. The exact story is your choice.

## Part 2: Guessing game

Implement:

```python
def guessing_game():
    """Run an interactive number-guessing game."""
```

The function must:

- Generate a secret integer from 1 through 100 with `random.randint`
- Repeatedly ask the user for a guess
- Print whether each incorrect guess is too low or too high
- Print a success message and stop after the correct guess

## Test locally

From the repository root:

```bash
uv run --directory week03 python -m pytest tests/ -v
```

The tests replace random numbers and keyboard input with predictable values.

## If a test fails

`pytest` prints the failing test's name, the line that failed, and the expected and actual
values. That is enough context for a coding agent to diagnose it: paste the full output into
Copilot CLI, Antigravity CLI, or a browser chat and ask what behavior the test expects and why
yours differs.

Ask for an explanation, not just a passing grade. You are responsible for every line you submit,
so make sure you can explain the fix before you commit it.

## Submit

```bash
git add week03/lab03.py
git commit -m "Complete Lab 03"
git push origin main
```

A green Week 03 badge earns 10 points.
