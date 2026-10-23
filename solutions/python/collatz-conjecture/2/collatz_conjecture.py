"""This is a Collatz Conjecture Puzze"""
def steps(number):
    """
    The function calculates the number of times the puzzle has to solve to get to 1.
    Args:
        number(int): number for solving the puzzle
    Returns:
        int: the number of steps to calcuate to solve the puzzle."""
    times = 0
    if number <=0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number /= 2
            times += 1
        else:
            number = (number * 3) + 1
            times += 1
    return times
            
            
            
