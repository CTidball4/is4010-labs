def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"Once upon a time, there was a {adjective} {noun} who loved to {verb} all day long."
import random

def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)
    guess = None
    while guess != secret:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct! You got it!")