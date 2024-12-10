# brain_games/scripts/brain_calc.py

import prompt
import random

def main():
    ROUNDS_COUNT = 3



    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    print("What is the result of the expression?")


    for i in range(ROUNDS_COUNT):
        question, result = randomaizer()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer != result:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.) ")
            print(f"Let's try again, {name}!")
            return

        else:
            print("Correct!")

    print(f"Congratulations, {name}!")






def randomaizer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        question = (f"{number1}{operator}{number2}")
        result = number1 + number2
    elif operator == '-':
        question = (f"{number1}{operator}{number2}")
        result = number1 - number2
    elif operator == '*':
        question = (f"{number1}{operator}{number2}")
        result = number1 * number2
    
    return question, str(result)




if __name__ == "__main__":
    main()
