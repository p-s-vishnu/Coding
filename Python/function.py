# leap year function
def is_leap(year):
    leap = False
    
    if year%100 == 0:
        return year%400 == 0
    else:
        return year%4 == 0
    
    return leap