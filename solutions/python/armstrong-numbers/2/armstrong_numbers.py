"""For each digit in the number, we raise it to the power of the number of digits in the number. If the sum of all these values is equal to the original number, the function returns True."""

def is_armstrong_number(number):
    
    """This works because we iterate through the actual digits of the number using for digit in str(number) or, in our case, for digit in new_number. We do not use range() here, because range(len(str(number))) would iterate over the indices (such as 0, 1, 2, ...) rather than the digits themselves. As a result, the program would raise the indices to a power instead of raising each digit of the number to that power, which would produce an incorrect result."""
    
    new_number = str(number)
    square_each = len(new_number)
    total = 0

    for digit in new_number:
        total += int(digit) ** square_each

    return total == number
        
