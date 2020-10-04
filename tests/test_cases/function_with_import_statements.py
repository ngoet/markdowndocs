import numpy as np
from typing import List


def generate_random_sequence(min_num: int, max_num: int, n: int) -> List[float]:
    """
    Generate random sequence of numbers, drawn from uniform distribution.

    :param min_num: Minimum value.
    :param max_num: Maximum value.
    :param n: Number of observations.
    :return: A list of float values between min_num and max_num, of length n.
    """
    return list(np.random.uniform(min_num, max_num, n))
