"""Determining a number is 'perfect' or 'abundant' or 'deficient'"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factors = 0
    for num in range(1, number):
        if number % num == 0:
            factors += num

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number < factors:
        return "abundant"
    if number  == factors:
        return "perfect"
    return "deficient"
            
            