def leapYear(x):
    if (x % 4) == 0:
        if(x % 100) == 0:
            return("Not a leap year")
        else:
            return("Leap year")
