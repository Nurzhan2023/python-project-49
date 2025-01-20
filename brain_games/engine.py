# brain_games/engine.py

import prompt
from brain_games.cli import welcome_user


def run_game(game, question):
    name = welcome_user()
    print(question)
    ROUNDS_COUNT = 3

    for i in range(ROUNDS_COUNT):
        question, result = game()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer != str(result):
            print(
                    f"'{answer}' is wrong answer ;(."
                    f"Correct answer was '{result}'.)"
                )

            print(f"Let's try again, {name}!")
            return


        print("Correct!")


    print(f"Congratulations, {name}!")
