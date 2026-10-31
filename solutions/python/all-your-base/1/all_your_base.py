"""Converting a sequence of digits in one base, representing
    a number, into a sequence of digits into another base.
"""

def rebase(input_base, digits, output_base):
    """
    Parameter:
        input_base(int): the input digit base
        digits(list): digits of the input
        output_base(int): the output of the digit base
    Returns:
        list: output_base digits
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")
        
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    decimal_number = 0
    result = []
    for index, digit in enumerate(digits):
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal_number += digit * input_base ** (len(digits) - index -1)
        
    if decimal_number == 0:
        return [0]
            
    while decimal_number > 0:
        remainder = decimal_number % output_base
        result.append(remainder)
        decimal_number = decimal_number // output_base

    return result[::-1]