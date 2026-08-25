"""Target score by points in radius"""

def score(x, y):
    
    """We make our other side (1,5,10) **2"""
    
    distance_squared = x**2 + y**2
    if distance_squared <= 1:
        return 10
    elif distance_squared <= 25:
        return 5
    elif distance_squared <= 100:
        return 1
    return 0
 

    
