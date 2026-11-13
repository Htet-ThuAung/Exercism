"""Encoding and Decoding the Atash cipher letter"""

def encode(plain_text):
    """
    Encode the cipher letter
    Parameter:
        plain_text(str): the string to encode
    Return:
        str: encoded string
    """
    
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = plain[::-1]
    mapping = dict(zip(plain, cipher))
    
    encoded = "".join(
        mapping[char] if char.isalpha()
        else char for char in plain_text.lower()
        if char.isalpha() or char.isdigit())
    
    return " ".join(encoded[index:index+5] 
                    for index in range(0, len(encoded), 5))

def decode(ciphered_text):
    """Decoding string from cipher
    Parameter:
        ciphered_text: encoded ciphered test
    Return:
        str: decoded string
    """
    
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = plain[::-1]
    mapping = dict(zip(cipher, plain))

    return "".join(
        mapping[char] if char.isalpha() else char
        for char in ciphered_text.lower()
        if char.isalpha() or char.isdigit()
    )