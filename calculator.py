# Addition function (returns the sum of first and second)

def add( first, second):
    return first + second



# Subtraction function (returns the difference between first and second)

def subtract( first, second):
    return first - second



# Multiplication function (returns the product of first and second)

def multiply( first, second):
    return first * second



# Division function (returns the quotient of first and second)

def divide( first, second):
    if second == 0:
    #checks the second number to see if it is zero
        raise Exception('I\'m sorry, I can\'t divide by zero')
    #defines what is in parantheses as the except statement (object) 
    try:
        return first / second
    #attempts to returns the quotient of first and second (will succeed if second num isn't 0)
    except Exception as err:
    #stores the except statement (object) in a variable named err
        return print(str(err))
    #returns exception statement(object) onverted to a str and passed to a print function for proper display
