import random


def gcd(a, b):   
    while b:
        a, b = b, a % b
    return a


def gcd_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = gcd(number1, number2)
    question = f"{number1} {number2}"
    return question, str(result)
