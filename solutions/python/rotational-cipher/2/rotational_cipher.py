"""For each char we need to check its index in alphabit, add key to this int and then add this char with new index from alpgabit into our new str and return it in the end"""

def rotate(text, key):
    """%26 let us come back to index 0 (a) and start proccess again, z is 25th index as we start from 0. Line 11 as in alphabit all lowercase, we take this uppercase, make it lower and after all upper again"""
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
            
