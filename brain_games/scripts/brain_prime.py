# brain_games/scripts/brain_prime.py


import random
import prompt



def main():
    ROUNDS_COUNT = 1


    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "Yes" if given number is prime. Otherwise answer "no".')


    for i in range(ROUNDS_COUNT):
        question, correct_answer = prime()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ").strip().lower()

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print (f"Let's try again, {name}!")
            return

        else:
            print("Correct!")



def prime():
    number = random.randint(1, 100)
    question = str(number)

    
    if number <= 1:
        correct_answer = "no"
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                correct_answer = "no"
                break
        else:
            correct_answer = "yes"

    return question, correct_answer




if __name__ == "__main__":
    main()
