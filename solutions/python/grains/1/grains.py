def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)

def total():
    # return 2**64 - 1 # Сумма геометрической прогрессии.
    
    result = 0
    
    for i in range(64):
        result += 2 ** i
        
    return result
    # 64, потому что начинается с нуля и если будет 65, то 64 уже будет как 65-ое значение
        
