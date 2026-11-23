#Defining the function
def name():
    print("kushal")

name()


#Giving a parameter to a function
def val(h):
    print(h)

val(12)


#Different ways of assigning values to the parametres
def add(a, b):
    print(a+b)

add(2,3)


def sub(c, d):
    print(c-d)

sub(3,5)


def minus(e, f):
    print(e-f)

minus(e=4,f=2)



#Return values
def plus(j, k):
    return j+k

total = plus(5,9)
print(total) 
print(plus(7,6)*(total))


#The final output for print total is None because nothing is being returned to total so it is none
def plus(l, m):
    print(l+m)

total = plus(5,9)
print(total) 



#To demonstrate how return works we can remove print total beacuse it was never need as the operation of printing was in function itself
def plus(l, m):
    print(l+m)

total = plus(8,8)



#Even or not

def even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(even(9))
print(even(8))


#Returning multiple values

def min_max(a, b):
    return min(a, b), max(a, b)

print(min_max(9, 3))



#default arguments
#Rule is the parameter with default argument should always be written after the parameter with the defult argument
def greet(name, greeting="Hello"):
    print(f'{name} {greeting}')

greet("Kushal","Welcome")
greet("Kushal")


#example of not using list or dict as a default argument
def dog(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(dog(3))



#SCOPE
#scope is where the variables live
#A variable created indside a function can be accessed only when that function is called as it lives inside that function only
#A variable declared outside the function is global and can be accessed anutime and anywhere

"""
x=10
def fun():
    y = 15

print(x)
print(y)



x=10
def fun(y=10):
    return y

print(fun(x))
print(fun(y)) """


#Here z value is 17 only when function is called otherwise it is 10 as declared outside function which acts as global varaible
z=10
def func():
    z = 17
    print(z)

func()
print(z)


#DOCSTRING

def area(r):
    """Return's the area of the circle with the given radius"""

    return 3.14159 * r * r

print(area(7))


#Calling a function from another function

def square(n):
    """Returns the square of the given number"""
    return n * n

def sum_of_squares(a, b):
    """Returns the sum of the given two numbers"""

    return square(a)+square(b)


print(sum_of_squares(3, 4))



#running a code only when I run this file directly, not when another file imports it

def add(a, b):
    """Returns the sum of given numbers"""
    return a + b

if __name__ == "_main_":
    print(add(2,3))

    


















