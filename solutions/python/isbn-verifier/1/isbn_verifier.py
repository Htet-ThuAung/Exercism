"""
ISBN verification process to identify a valid ISBN or Not

"""
def is_valid(isbn):
    """
    Paramenters:
        isbn(str):
            isbn for validation
            
    Return:
        bool:
            True if it is a vlaid isbn otherwise False
    """
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == "X"):
        return False

    digits = [int(digit) for digit in isbn[:9]]
    digits.append(10 if isbn[9] == "X" else int(isbn[9]))

    result = 0

    for index, digit in enumerate(digits):
        result += digit * (10 - index)

    return result % 11 == 0
