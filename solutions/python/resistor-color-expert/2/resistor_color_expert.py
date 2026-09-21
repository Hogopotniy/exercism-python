"""Two dictionaries, for 4-5 inputs of colors and transforming into human language"""

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
    "white" : 9,
}

TOLERANCE = {
    "grey" : "±0.05%",
    "violet" : "±0.1%",
    "blue" : "±0.25%",
    "green" : "±0.5%",
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver" : "±10%"
}

def resistor_label(colors):

    """Define 0, that if len 4 or 5 do what is below, 
    :g --- Removes unnecessary zeros after division."""

    if len(colors) == 1:
        return "0 ohms"

    first = COLORS[colors[0]]
    second = COLORS[colors[1]]
    tolerance = TOLERANCE[colors[-1]]
    
    if len(colors) == 5:
        third = COLORS[colors[2]]
        fourth = COLORS[colors[3]]
        value = first * 100 + second * 10 + third
        resistance = value * (10 ** fourth)
        
    elif len(colors) == 4:
        third = COLORS[colors[2]]
        value = first * 10 + second
        resistance = value * (10 ** third)


    # if resistence >= 1_000_000:
    #     return f"{resistence / 1_000_000:g} megaohms {tolerance}"

    # if resistence >= 1_000:
    #     return f"{resistence / 1_000:g} kiloohms {tolerance}"

    # else:
    #     return f"{resistence} ohms {tolerance}"

    if resistance >= 1_000_000:
        resistance = resistance / 1_000_000
        unit = "megaohms"

    elif resistance >= 1_000:
        resistance = resistance / 1_000
        unit = "kiloohms"

    else:
        unit = "ohms"

    return f"{resistance:g} {unit} {tolerance}"

    