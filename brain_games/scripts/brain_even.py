# brain_games/scripts/brain_even.py
import prompt
import random


def main():
    ROUNDS_COUNT = 3


    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')


    for i in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return


        else:
            print("Correct!")

    
    print(f"Congratulations, {name}!")


def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number %2 == 0 else "no"
    return question, correct_answer


if __name__ == "__main__":
    main()






