# Lab 02: AI-generated Python preview

**Due:** Sunday at 11:59 PM  
**Points:** 10

Formal Python instruction begins next week. In this lab, you will treat Python as an artifact produced by an AI coding assistant: describe behavior, run objective tests, and improve your prompts until the generated code meets its contract. You are not expected to know every Python construct yet.

You may use GitHub Copilot, ChatGPT, Gemini, Claude, or another coding assistant available to you.

## Deliverables

Create exactly these files:

- `week02/lab02.py`
- `week02/lab02_prompts.md`, copied from `lab02_prompts.template.md`

Do not modify the tests, workflow, templates, or lab instructions.

## Function contracts

Ask your assistant to implement these functions in `lab02.py`:

```python
def make_greeting(name: str) -> str:
    """Return exactly 'Hello, NAME!' using the supplied name."""


def is_even(number: int) -> bool:
    """Return True when number is even and False otherwise."""


def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""
```

The functions must also handle empty strings, multiword names, negative integers, zero, uppercase vowels, and text containing no vowels.

## Prompt experiment

For each function:

1. Write an initial prompt in your own style and record it.
2. Ask the assistant to generate the function.
3. Run the tests.
4. Rewrite the prompt using Context, Persona, Task, and Format (CPTF).
5. Apply the improved result and run the tests again.

Run the complete grader from the repository root:

```bash
PYTHONPATH=week02 pytest week02/tests/ -v
```

If a test fails, include the failure message in your next prompt. Do not ask the assistant merely to "make the tests pass"; explain the intended behavior and ask it to diagnose the mismatch.

## Submission

```bash
git add week02/lab02.py week02/lab02_prompts.md
git commit -m "Complete Lab 02 AI experiment"
git push origin main
```

The Week 02 workflow validates both the Python behavior and completion of the prompt journal. A green badge earns 10 points.
