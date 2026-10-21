def leap_year(year):
    """
    Return the calculate leap year or not
    
    Parameters:
        year(int): the year to calcuate the leap year or not
    
    Returns:
        True if the year is leap year or Flase otherwise.
        """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
