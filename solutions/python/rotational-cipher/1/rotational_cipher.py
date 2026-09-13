"""For each char we need to check its index in alphabit, add key to this int and then add this char with new index from alpgabit into our new str and return it in the end"""

def rotate(text, key):
    new_text = ""
    alphabit = "abcdefghijklmnopqrstuvwxyz"

    for char in text:
        if char.isalpha():
            if char.isupper():
                new_text += alphabit[(alphabit.index(char.lower()) + key) % 26].upper()
            else:
                new_text += alphabit[(alphabit.index(char) + key) % 26]
        else:
            new_text += char

    return new_text
            
