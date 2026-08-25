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
    
    