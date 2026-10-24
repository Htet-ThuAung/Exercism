"Converting a number into its corresponding raindrops sound."
def convert(number):
    """
    Args:
        number(int): The number to convert sound.
    Return:
        "Pling" if divisible by 3
        "Plang" if divisible by 5
        "Plong" if divisible by 7
        "str(number)" if not 3 above
    """
    div_3 = number % 3 == 0
    div_5 = number % 5 == 0
    div_7 = number % 7 == 0
    if div_3 and div_5 and div_7:
        return "PlingPlangPlong"
    if div_3 and div_5:
        return "PlingPlang"
    if div_3 and div_7:
        return "PlingPlong"
    if div_5 and div_7:
        return "PlangPlong"
    if div_3:
        return "Pling"
    if div_5:
        return "Plang"
    if div_7:
        return "Plong"
    return str(number)
