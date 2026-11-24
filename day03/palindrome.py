from reverse_num import is_reverse

def is_palindrome(n):
    
    """Tells whether the given number is palindrome or not"""

    return is_reverse(n) == n

if __name__ == "__main__":

    n = int(input("Enter a number to check if it is palindrome or not:"))
    if is_palindrome(n):
        print("Given number is palinrome number")
    else:
        print("Given number is not a palindrome number")


