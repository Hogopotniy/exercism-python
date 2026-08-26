"""We don't need this func and exception mesxages, but I decided to add"""

def valid_triangle(sides):

    a = sides[0]
    b = sides[1]
    c = sides[2]

    # a, b, c = sides --- We can do this way as well

    # if a <= 0 or b <= 0 or c <= 0:
    #     raise ValueError("all inputs should be more that 0!")

    # if not (
    #     a + b >= c 
    #     and b + c >= a 
    #     and a + c >= b
    # ):
    #     raise ValueError("invalid triangle!")

    # return True
    

    return (
        a > 0
        and b > 0
        and c > 0
        and a + b >= c
        and b + c >= a
        and a + c >= b
    )

    
def equilateral(sides):
    """All three sides same length"""
    if not valid_triangle(sides):
        return False
        
    a, b, c = sides
    return a == b == c
        

def isosceles(sides):
    """At least 2 sides same length"""
    if not valid_triangle(sides):
        return False
        
    a, b, c = sides
    return a == b or a == c or b == c


def scalene(sides):
    """All three sides different length"""
    if not valid_triangle(sides):
        return False
        
    a, b, c = sides
    return a != b and a != c and b != c

    
