import random

def calc_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        question = f"{number1} {operator} {number2}"
        result = number1 + number2
    elif operator == '-':
        question = f"{number1} {operator} {number2}"
        result = number1 - number2
    else:
        question = f"{number1} {operator} {number2}"
        result = number1 * number2

    return question, str(result)

