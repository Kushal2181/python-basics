#Leap year program
#If a certain year is divisible by 4, then it is a leap year. But if the year is divisible by 100, then it is not a leap year unless it is also divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:  
    print(year, "is not a leap year.")