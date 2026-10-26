"""Determining a word or phrase is an isogram or not"""
def is_isogram(phrase):
    """Parameters:
        phrase:
            the word or phrase to determine isogram or not
    Returns:
        bool:
            return True if it is isogram otherwise False
    """
            
    letter = [ch.lower() for ch in phrase if ch.isalpha()]
    return len(letter) == len(set(letter))