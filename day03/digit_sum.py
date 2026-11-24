def digit_sum(n):
    """Gives the sum of digits of a given number"""

    original = n
    sum = 0
    ctr = 0

    temp = n
    while temp>0:
        temp = temp//10
        ctr+=1

    num = n
    for i in range(ctr):
        digit = num%10
        num = num//10
        sum = sum+digit

    return sum

if __name__ == "__main__":

    n = int(input("Enter a number to find the sum of its digits:"))
    print(f"The sum of digits of {n} is ",digit_sum(n))
