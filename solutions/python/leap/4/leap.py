def leap_year(year):
    """
    Return boolean value that the calculated year is leap year or not
    
    Parameters:
        year(int): the year to calcuate the leap year or not
    
    Returns:
        True if the year is leap year or Flase otherwise.
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
