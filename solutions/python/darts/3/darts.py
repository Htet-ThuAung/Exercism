"""Calculating the point scored in a single toss of a Darts game"""
import math
def score(x, y):
    """
    Parameter:
        x, y (int): the corrdinate of the dart land.
    Returns:
        score (int): the point got depending upon when the dart land.
        """
    outer_circle_point = 1
    middle_circle_point = 5
    inner_circle_point = 10
    dart_land = math.sqrt(x**2 + y**2)
    if dart_land <= 1:
        return inner_circle_point
    if dart_land <= 5:
        return middle_circle_point
    if dart_land <= 10:
        return outer_circle_point
    return 0