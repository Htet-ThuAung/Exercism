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
    radius = math.sqrt(x**2 + y**2)
    if radius <= 1:
        return inner_circle_point
    if radius <= 5:
        return middle_circle_point
    if radius <= 10:
        return outer_circle_point
    return 0