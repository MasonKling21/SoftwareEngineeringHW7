def fizzedBuzz(x):
    if(type(x) != int):
        print("Error!")
        return("Error!")
    elif (x % 3) == 0 and (x % 5) == 0:
        print("FizzBuzz")
        return("FizzBuzz")
    elif (x % 3) == 0:
        print("Fizz")
        return("Fizz")
    elif (x % 5) == 0:
        print("Buzz")
        return("Buzz")
    else:
        print(x)
        return(x)
