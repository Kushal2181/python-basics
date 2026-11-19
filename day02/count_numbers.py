n = 1
ctr1 = 0
ctr2 = 0
while n!=0:
    n = int(input("Enter a number:"))

    if n>0:
        ctr1 = ctr1+1
    elif n<0:
          ctr2 = ctr2+1

print(f"No of positive integers are",ctr1)
print(f"No of negative integers are",ctr2)