"""Determine whether the year is a leap year or not"""
def leap_year(year):
    """
    Return boolean value that the calculated year is leap year or not
    
    Args:
        year(int): the year to check
    
    Returns:
        bool: True if the year is leap year or Flase otherwise
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
