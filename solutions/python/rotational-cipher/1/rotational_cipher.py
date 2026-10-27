"""An implementation of the rotation cipher.
    """
def rotate(text, key):
    """
    Parameter:
        text(str): the string to rotate
        key(int): the acquired shifted Key
    Return:
        result(str): the output result of rotation cipher
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index + key) % 26
            rotated = alphabet[new_index]

            if char.isupper():
                rotated = rotated.upper()

            result += rotated
        else:
            result += char

    return result