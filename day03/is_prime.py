def is_prime(n):
    """Tells whether the given number is prime or not"""

    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":

    n = int(input("Enter a number to check if it is prime or not:"))

    if is_prime(n):
        print("Given number is prime number")
    else:
        print("Given number is not a prime number")

