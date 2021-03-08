def leapYear(x):
    if(type(x) != int):
        return("Error!")
    if (x % 4) == 0:
        if(x % 400) == 0 or (x % 100) != 0:
            return("Leap year")
        else:
            return("Not a leap year")
    else:
        return("Not a leap year")
