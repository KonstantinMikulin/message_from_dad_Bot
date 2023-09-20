from random import randint


# Function for getting random value from any dictionary
def get_random_value(dictionary: dict) -> str:
    key = randint(1, len(dictionary))

    return dictionary[key]
