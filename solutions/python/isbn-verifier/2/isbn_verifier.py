"""ISBN validity test"""

def is_valid(isbn):

    """Working solution"""
    
    isbn = isbn.replace("-", "")
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    times = 10
    if len(isbn) == 10:
        for i in isbn:
            if i not in alph:
                result += int(i) * times
                times = times - 1
            elif i in "xX":
                result += 10 * times
            else:
                return False
    else:
        return False
    return result % 11 == 0
                
                
