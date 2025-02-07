import random


def get_random_pairs(nr_of_pairs: int) -> list[int]:
    # Create a list of pairs of identical integers
    pairs = [[i] * 2 for i in range(nr_of_pairs)]

    # Flatten the list of pairs into a single list
    numbers = [num for pair in pairs for num in pair]

    # Shuffle the list to randomly distribute the pairs
    random.shuffle(numbers)

    return numbers


