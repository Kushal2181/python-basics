def is_reverse(num):
    """Gives the reverses version of the given number"""


    original = num
    rev = 0
    ctr = 0

    num_1 = num
    while num_1 >  0:
        num_1 = num_1 // 10
        ctr+=1

    temp = num
    for _ in range(ctr):
        a = temp%10
        rev = rev*10 + a
        temp = temp//10


    return rev


if __name__ == "__main__":

    num = int(input("Enter a number to display it's reversed version:"))
    print(is_reverse(num))