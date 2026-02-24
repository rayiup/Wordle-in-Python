import random

WORD_LENGTH = 5
MAX_ATTEMPTS = 6

# Curated list of common 5-letter words.
WORDS = [
    "apple", "beach", "brain", "chair", "cloud", "crane", "dance", "dream",
    "earth", "flame", "grape", "house", "light", "mouse", "ocean", "pearl",
    "plant", "queen", "river", "round", "smile", "sound", "stone", "table",
    "tiger", "train", "water", "world", "zebra",
]


def score_guess(guess: str, answer: str) -> list[str]:
    """Return a list of statuses: 'correct', 'present', or 'absent'."""
    result = ["absent"] * WORD_LENGTH
    remaining_answer_chars: dict[str, int] = {}

    # First pass: exact matches.
    for i, char in enumerate(guess):
        if char == answer[i]:
            result[i] = "correct"
        else:
            remaining_answer_chars[answer[i]] = remaining_answer_chars.get(answer[i], 0) + 1

    # Second pass: present but in wrong place.
    for i, char in enumerate(guess):
        if result[i] != "correct" and remaining_answer_chars.get(char, 0) > 0:
            result[i] = "present"
            remaining_answer_chars[char] -= 1

    return result


def format_feedback(guess: str, result: list[str]) -> str:
    """Pretty print feedback using emoji squares."""
    mapping = {
        "correct": "🟩",
        "present": "🟨",
        "absent": "⬛",
    }
    tiles = "".join(mapping[state] for state in result)
    return f"{guess.upper()}  {tiles}"


def get_valid_guess() -> str:
    while True:
        guess = input("Enter a 5-letter guess: ").strip().lower()
        if len(guess) != WORD_LENGTH or not guess.isalpha():
            print("Please enter exactly 5 letters.")
            continue
        return guess


def play_wordle() -> None:
    print("Welcome to Wordle (Python Edition)!\n")
    answer = random.choice(WORDS)

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"Attempt {attempt}/{MAX_ATTEMPTS}")
        guess = get_valid_guess()
        result = score_guess(guess, answer)
        print(format_feedback(guess, result))
        print()

        if guess == answer:
            print(f"🎉 You won in {attempt} attempt(s)! The word was '{answer.upper()}'.")
            return

    print(f"😢 Out of attempts. The word was '{answer.upper()}'.")


if __name__ == "__main__":
    play_wordle()
