import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):  # Generate 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        if ask_question(x, y):
            score += 1

    print(f"Score: {score}")


def get_level():
    """
    Prompt the user for a level (1, 2, or 3).
    Re-prompt until a valid level is provided.
    """
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        print("Invalid level. Please enter 1, 2, or 3.")


def generate_integer(level):
    """
    Generate a random integer with the number of digits corresponding to the level.
    Raise ValueError if the level is not 1, 2, or 3.
    """
    if level == 1:
        return random.randint(0, 9)  # 1-digit numbers
    elif level == 2:
        return random.randint(10, 99)  # 2-digit numbers
    elif level == 3:
        return random.randint(100, 999)  # 3-digit numbers
    else:
        raise ValueError("Invalid level")


def ask_question(x, y):
    """
    Prompt the user to solve the problem x + y = .
    Allow up to three attempts. Display the correct answer after three failed attempts.
    Return True if the user answers correctly, False otherwise.
    """
    attempts = 0
    correct_answer = x + y

    while attempts < 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == correct_answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")
        attempts += 1

    print(f"{x} + {y} = {correct_answer}")
    return False


if __name__ == "__main__":
    main()
