
def factorial(n):
    """Returns the factorial of the given number"""

    fact = 1
    if n>0:

       for i in range(1,n+1):
            fact = fact * i

       return fact

    else:
        print("Enter a number greater than 0")
        


b = int(input("enter a number to find its factorial:"))
print(factorial(b))





