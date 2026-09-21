"""First two colors as number, rest 10 ** 3, than conditions and result"""

COLORS = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6,
    "violet" : 7,
    "grey" : 8,
    "white" : 9
}



def label(colors):

    """Can be done using cicle, list or just return(str(..)) and so on"""

    result = []
    
    first = COLORS[colors[0]]
    second = COLORS[colors[1]]
    third = COLORS[colors[2]]

    value = first * 10 + second
    resistance = value * (10 ** third)

    if resistance >= 1_000_000_000:
        return str(resistance // 1_000_000_000) + " gigaohms"
    
    elif resistance >= 1_000_000:
        return str(resistance // 1_000_000) + " megaohms"
     
    elif resistance >= 1_000:
        result.append(str(resistance // 1_000)) 
        result.append("kiloohms")
      
    else:
        result.append(str(resistance)) 
        result.append("ohms")

    return " ".join(result)


        
