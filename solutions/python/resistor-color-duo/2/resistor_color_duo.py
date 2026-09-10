"""We create a list of colors, by default as in list, they have their indexes. Our mission i  case of two colors or more, calc combine two indexes and get a whole number, like '1' + '5' = '15'"""

COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

def value(colors):
    if len(colors) == 1:
        return COLORS.index(colors[0])
    return COLORS.index(colors[0]) * 10  + COLORS.index(colors[1])

