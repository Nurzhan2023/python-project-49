# brain_games/scripts/brain_gcd.py

import random
import prompt
import math

def main():
    ROUNDS_COUNT = 3

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    print ("Find the greatest common divisor of given numbers.")

    for i in range(ROUNDS_COUNT):

        number1, number2 = find_divisor()
        correct_answer = math.gcd(number1, number2)

        print(f"Question: {number1} {number2}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")

        else:
            print(f"'{user_answer}' is wrong answer ;(.Correct answer was '{correct_answer}'. ")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")





def find_divisor():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return number1, number2 










if __name__ == "__main__":
    main()
