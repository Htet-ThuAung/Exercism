"""Determining what Bob will reply to someone when they ask something to him
or ask a question."""
def response(hey_bob):
    """
    Args:
        hey_bob(str): A string whether a question or a conversion.
    Return:
        str: responsible feedback string from bob.
    """
    if hey_bob.strip().endswith("?") and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.strip().endswith("?"):
        return "Sure."
    elif hey_bob.strip() == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."