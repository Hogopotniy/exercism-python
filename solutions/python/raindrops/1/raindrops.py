"""Conditions"""

def convert(number):
    # if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
    #     return "PlingPlangPlong"
    # if number % 3 == 0 and number % 5 == 0:
    #     return "PlingPlang"
    # if number % 3 == 0 and number % 7 == 0:
    #     return "PlingPlong"
    # if number % 5 == 0 and number % 7 == 0:
    #     return "PlangPlong"
    # if number % 3 == 0:
    #     return "Pling"
    # if number % 5 == 0:
    #     return "Plang"
    # if number % 7 == 0:
    #     return "Plong"
    # return str(number)

    """We could do in a much better way"""

    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    # if result: --- фактически означает "если строка не пустая"
    #     return result
    # else:
    #     return str(number)

    return result if result else str(number)
    # значение_если_True if условие else значение_если_False