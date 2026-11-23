def is_armstrong(num):
    """Finds whether the given number is armstrong or not"""
    ctr = 0
    total = 0
    original = num

    temp = num
    while temp>0:
        temp = temp // 10
        ctr+=1

    num1 = num
    for _ in range(ctr):
        b = num1 % 10
        c = b ** ctr
        num1= num1//10
        total = total + c

        

    return total == original


if __name__ == "__main__":

    num = int(input("Enter a number to check if it is armstrong or not:"))
    if is_armstrong(num):
        print("Number is armstrong")
    else:
        print("Number is not armstrong")








