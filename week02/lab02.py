def make_greeting(name: str) -> str:
    """Return exactly 'Hello, NAME!' using the supplied name."""
    return f"Hello, {name}!"


def prompt_for_name() -> str:
    """Prompt for a name and return a greeting."""
    name = input("What is your name? ")
    return f"Hello {name}"


def is_even(number: int) -> bool:
    """Return True when number is even and False otherwise."""
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count a, e, i, and o without regard to case; do not count y."""
    return sum(character.lower() in "aeio" for character in text)