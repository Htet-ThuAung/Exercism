"""Print the color code value on the resistor."""
def resistor_label(colors):
    """
    Parameters:
        colors (list): The input colors
    Return:
        The representative resistance value
    """

    # Handle special case
    if len(colors) not in (1,4, 5):
        raise ValueError("Invalid number of resistor colors")
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    color_names = color_code()

    # Determine the significant digits and multiplier
    if len(colors) == 4:
        first_value = color_names.index(colors[0])
        second_value = color_names.index(colors[1])
        multiplier = color_names.index(colors[2])
        tolerance = tolerance_band(colors[3])

        values = (10 * first_value + second_value) * 10**multiplier

    if len(colors) == 5:
        first_value = color_names.index(colors[0])
        second_value = color_names.index(colors[1])
        third_value = color_names.index(colors[2])
        multiplier = color_names.index(colors[3])
        tolerance = tolerance_band(colors[4])

        values = (
            100 * first_value +
            10 * second_value +
            third_value
        ) * 10**multiplier

    # Convert resistance into appropriate units
    if values >= 10**9:
        return f"{values / 10**9:g} gigaohms ±{tolerance}"

    if values >= 10**6:
        return f"{values / 10**6:g} megaohms ±{tolerance}"

    if values >= 10**3:
        return f"{values / 10**3:g} kiloohms ±{tolerance}"

    return f"{values} ohms ±{tolerance}"


def color_code():
    """The colors allowed on the resistor."""

    return [
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


def tolerance_band(tolerance_color):
    """The resistor color code tolerance band."""
    tol_color = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }

    return tol_color[tolerance_color]