def square(number):
    """
    Calculate the number of grains on each chesssquare
    
    Args:
        number(int): the number of square on the chessboard
    Returns:
        int: the number of grains on each square of chessboard
        """
    if number >0 and number <= 2:
        return number
    elif number > 2 and number < 65:
        return 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    """
    Calculate the total number of grains on the chessboard
    
    Args: None
    Returns:
        The total number of grains on the chessboard"""
    result = 0
    for number in range(1, 65):
        result += square(number)
    return result
