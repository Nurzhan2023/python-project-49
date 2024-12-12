# brain_games/scripts/brain_prime.py
import random

import prompt


def main():
    ROUNDS_COUNT = 3
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(ROUNDS_COUNT):
        question, correct_answer = prime()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;"
                "(. Correct answer was '{correct_answer}'."
            )
            print (f"Let's try again, {name}!")
            return

        else:
            print("Correct!")
            
    print(f"Congratulations, {name}!")


def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False

    return True


def prime():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer


if __name__ == "__main__":
    main()
