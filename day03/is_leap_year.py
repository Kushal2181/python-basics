def is_leap(n):
    """Tells whether the given year is leap year or not"""

    if n%4==0 and n%100!=0:
        return True
    elif n%400==0:
        return True
    else:
        return False


if __name__ == "__main__":

    n = int(input("Enter a year to check if it is leap year or not:"))
    if is_leap(n):
        print("It is a Leap year")
    else:
        print("It is not a Leap year")

