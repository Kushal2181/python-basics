
def factorial(n):
    """Returns the factorial of the given number"""

    fact = 1
    

    for i in range(1,n+1):
        fact = fact * i

    return fact

   
        

if __name__ == "__main__":

    b = int(input("enter a number to find its factorial:"))
    print(factorial(b))





