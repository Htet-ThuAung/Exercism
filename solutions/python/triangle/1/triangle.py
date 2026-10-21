def equilateral(sides):
    """
    The triangle has all the same side lengths.
    
    Args:
        sides(int): the sides of the triangle
        
    Returns:
        bool: True if all the side lengths are same or False otherwise.
    """
    a, b, c = sides
    return a > 0 \
    and a + b >= c \
    and b + c >= a \
    and a + c >= b \
    and a == b == c


def isosceles(sides):
    """
    The triangle has 2 same length.
    
    Args:
        sides(int): the sides of the triangle
    Returns:
        Bool: True if it is a isosceles or False otherwise
    """
    a, b, c = sides
    return a > 0 \
    and a + b >= c \
    and a + c >= b \
    and b + c >= a \
    and (a == b or a == c or b == c)


def scalene(sides):
    """
    The triangle has different lengths.
    
    Args:
        sides(int): the side of triangle
    Returns:
        bool: True if all sides has different lengths, or False otherwise."""
    a, b, c = sides
    return a > 0 \
    and a + b >= c \
    and a + c >= b \
    and b + c >= a \
    and (a != b and a!= c and b != c)
    
