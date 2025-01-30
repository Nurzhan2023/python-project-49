import random


QUESTION = "What is the result of the expression?"


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    question = f"{number1} {operator} {number2}"
    return question, str(result)

