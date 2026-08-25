def is_isogram(phrase):
    phrase = phrase.lower()
    letter = ""
    for char in phrase:
        if char.isalpha():
            if char in letter:
                return False
            letter += char
    return True
    
    