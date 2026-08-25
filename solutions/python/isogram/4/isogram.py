"""Need to return True or False for is_isogram()"""

def is_isogram(phrase):
    """Solution below"""
    phrase = phrase.lower()
    letter = ""
    for char in phrase:
        if char.isalpha():
            if char in letter:
                return False
            letter += char
    return True

    # Another harder, but more Python version
    # letters = [c.lower() for c in phrase if c.isalpha()]
    # return len(letters) == len(set(letters))
    
    