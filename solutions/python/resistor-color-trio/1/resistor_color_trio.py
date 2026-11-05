def label(colors):
    color_names = color_code()
    first_value = color_names.index(colors[0])
    second_value = color_names.index(colors[1])
    third_value = color_names.index(colors[2])
    values = (10 * first_value + second_value )* 10**third_value
    if values >= 10**9:
        return f"{values // 10**9} gigaohms"
    if values >= 1000000:
        return f"{values//10**6} megaohms"
    if values >= 1000:
        return f"{values//10**3} kiloohms"
    return f"{values} ohms"


def color_code():
    color = [
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
    return color
