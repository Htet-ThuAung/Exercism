""" Translating to Pig Latin Language
Rules:
    1. If the word starts with vowel or 'xr' or 'yt',
        add 'ay' at the end.
    
    2. If the word start with consonant and found a vowel,
        move the previous alphabet to the end and add 'ay' at the end.
    
    3. If 'qu' found in the word, move the consonants to the end and
        add 'ay'.

    4. If 'y' found in the word, move the previous consonants to the end         and add 'ay'.
    """

def translate(text):
    """
    This function translates the Pig Latin Language.
    
    Args:
        text(str): word to translate
    Returns:
        str: the translated result
    """
    vowel = "aeiou"
    translated_word = []
    for word in text.split():
        if word[0] in vowel or text.startswith(("xr", "yt")):
            translated_word.append(text + "ay")
            continue

        idx = 0
        while idx < len(word):
            if word[idx: idx + 2] == "qu":
                idx += 2
                break

            if word[idx] in vowel or( word[idx] == "y" and idx > 0):
                break
            idx += 1

        translated_word.append(word[idx:] + word[:idx] + "ay")

    return " ".join(translated_word)

