
def is_armstrong_number(number):
    new_number = str(number)
    square_each = len(new_number)
    total = 0

    for digit in new_number:
        total += int(digit) ** square_each

    return total == number
        
