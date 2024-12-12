# brain_games/scripts/brain_progression.py
import random

import prompt


def main():
    ROUNDS_COUNT = 3
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for a in range(ROUNDS_COUNT):
        progression, correct_answer = generate_progression()
        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")

        else:
            print(
                f"'{user_answer}' is wrong answer ;"
                "(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def generate_progression():

    start = random.randint(1, 10)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length -1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, hidden_value


if __name__ == "__main__":
    main()
