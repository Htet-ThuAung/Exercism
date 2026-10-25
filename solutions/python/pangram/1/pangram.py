""" This function defines Pangram which means every letter 
    in the alphabet has to be appeared at least once in the              sentence."""
def is_pangram(sentence):
    """
    Parameter:
        Args:
            sentence(str): Theinput string.
        Return:
            bool: the result is Pangram or not
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = all(letter in sentence.lower() for letter in alphabet)
    return result
