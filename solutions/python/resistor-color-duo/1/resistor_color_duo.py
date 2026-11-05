"""Take the color as input and return two digit numbers as output"""
def value(colors):
    """
    Parameters:
        colors(str): the input color
        
    Returns:
        the two digit value(int): the sum of two digit number"""
    col = color_names()
    first_value = col.index(colors[0])
    second_value = col.index(colors[1])
    return 10 * first_value + second_value


def color_names():
    """
    The color names of the resistor"""
    color_name = [
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
    return color_name