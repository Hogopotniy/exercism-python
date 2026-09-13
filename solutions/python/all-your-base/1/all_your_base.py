"""We firsly make a base of 10 for each input and later comvert it into output one"""

def rebase(input_base, digits, output_base):

    """We need //= to decrase the result otherwise it would be infinite, also we use lisy(reversed(..)) because reversed() don't create a new list and return iterators, but we could make full_result.reverse() and then return full_result. Also very important to check for 0 and return [0]"""

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    

    result = 0
    for index, num in enumerate(reversed(digits)):
        result += num * (input_base ** index)

    if result == 0:
        return [0]
        
    full_result = []
    while result >= 1:
        full_result.append(result % output_base)
        result //= output_base


    return list(reversed(full_result))

            
                
                
                
