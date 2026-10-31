"""Calculating the point scored in a single toss of a Darts game"""
import math
def score(x, y):
    """
    Parameter:
        x, y (int): the corrdinate of the dart land.
    Returns:
        score (int): the point got depending upon when the dart land.
        """
    radius = math.sqrt(x**2 + y**2)
    if radius <= 1:
        return 10
    if radius <= 5:
        return 5
    if radius <= 10:
        return 1
    return 0