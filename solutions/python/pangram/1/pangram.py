"""Pangram - check the meaning"""

def is_pangram(sentence):
    # sentence = sentence.lower()
    # output = "abcdefghijklmnopqrstuvwxyz"
    # result = ""
    # for char in sentence:
    #     if char in output:
    #         if char not in result:
    #             if char.isalpha():
    #                 result += char
    # return len(result) == 26

    """More advanced and shorter option"""

    letters = set()
    for char in sentence.lower():
        if char.isalpha():
            letters.add(char)
    return len(letters) == 26

    
