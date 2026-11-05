"""Looking up the resistor color code"""
def color_code(color):
    """
    Parameter:
        color(str): the color of the resistor
    Return:
        color_index(int): the index of the color
    """
    for color_index, color_name in enumerate(colors()):
        if color_name == color:
            return color_index
    return None

            
def colors():
    """List the color in a list"""
    colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return colors
    
