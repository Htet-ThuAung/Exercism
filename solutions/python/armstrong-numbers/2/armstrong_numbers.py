def is_armstrong_number(number):
    """
    Calculating the armstrong number
    Args:
        number(int): the number to calculate armstrong number or not
    Return:
        bool: True if the number is armstrong number otherwise False
    """
    armstrong_num = 0
    for num in range(len(str(number))):
        armstrong_num += int(str(number)[num])**len(str(number))
    return armstrong_num == number
