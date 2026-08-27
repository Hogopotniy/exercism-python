"""ISBN validity test"""

# def is_valid(isbn):

#     """Working solution"""
    
#     isbn = isbn.replace("-", "")
#     alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = 0
#     times = 10
#     if len(isbn) == 10:
#         for i in isbn:
#             if i not in alph:
#                 result += int(i) * times
#                 times = times - 1
#             elif i in "xX":
#                 result += 10 * times
#             else:
#                 return False
#     else:
#         return False
#     return result % 11 == 0

def is_valid(isbn):

    """More advanced solution in all ways"""
    
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    total = 0

    for position, char in enumerate(isbn):
        if char.isdigit():
            value = int(char)

        elif char == "X" and position == 9:
            value = 10

        else:
            return False

        total += value * (10 - position)

    return total % 11 == 0

                
                
