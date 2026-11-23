import math

#sqare of a given number

def square(n):
    """Returns the square of the given number"""
    return n * n

print(square(5))


#If a number is even or not

def even(n):
    """Returns if given number is even or not"""
    if n%2 == 0:
        return True
    else:
        return False

print(even(7))


#default argument program

def greet(name, greeting="Hello"):
    """Returns the default argument if one is not given by user as a greeting"""

    print(name,greeting)

greet("Kushal", "Welcome")
greet("Kushal")


#Finding smallest and largest of three numbers

def min_max(a,b,c):
    """Returns the smallest and largest of the given numbers"""

    return min(a,b,c), max(a,b,c)

print("Minimum and maximum of three numbers is:",min_max(3,6,2))



