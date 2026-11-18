a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)


import math

# Temperature converter
c = float(input("Enter temperature in Celsius: "))

fahrenheit = (c * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")



# Simple interest calculator
principal = float(input("Enter the principal amount :"))
time = float(input("Enter the time :"))
rate_of_interest = float(input("Enter the rate of interest :"))

simple_interest = (principal * time * rate_of_interest)/100
print(f"Simple interest : {simple_interest:.2f}")


# Area of circle
r = float(input("Enter radius of circle"))
Area = (math.pi)*r*r
print(f"Area of circle : {Area:.2f}")


# swapping two variables 
a = "apple"
b = "pie"
temp = a
a = b
b = temp

print(a,b) 


# Sum of digits
num = int(input("Enter a number: "))

a1=num%10
a2=num//10
b1=a2%10
b2=a2//10
c1=b2%10
c2=b2//10

total = a1+b1+c1
print(f"Sum of digits: {total}")





