import random


QUESTION = "What number is missing in the progression?"


def generate_question():   
    start = random.randint(1, 10)
    step = random.randint(2, 10)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = ".."
    progression_str = " ".join(map(str, progression))
    return progression_str, str(hidden_value)


