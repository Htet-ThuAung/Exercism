"""Verifying the brackets, braces, and parentheses match."""
def is_paired(input_string):
    """
    Parameter:
        input_string(str): string to validate the output
    Return:
        bool: True if the brackets match
    """
    stack = []
    matching_brackets = {
        ')': '(',
    ']': '[',
    '}':'{'
    }

    for char in input_string:
        if char  in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack:
                return False
            if stack.pop() != matching_brackets[char]:
                return False
    return len(stack) == 0