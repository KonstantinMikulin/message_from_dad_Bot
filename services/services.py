from random import randint


def get_random_value(dictionary: dict) -> str:
    key = randint(1, len(dictionary))

    return dictionary[key]
