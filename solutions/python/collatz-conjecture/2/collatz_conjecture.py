"""Need to use exception messages sometimes"""

def steps(number):
    """Sample of my solution"""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    times = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        times += 1
    return times
            
        