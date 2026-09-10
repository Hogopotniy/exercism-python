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

