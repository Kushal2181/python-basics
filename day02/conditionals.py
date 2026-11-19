
#directly assigning a true or false value and printing it
print("directly assigning a true or false value and printing it:")
is_sunny = True
print(is_sunny)
is_rainy = False
print(is_rainy) 


#checking whether a condition is true or false by using logicaloperators
print("\nchecking whether a condition is true or false by using operators:")
age = 21

print(age >= 18)
print(age <= 18)
print(age < 18)
print(age > 18)
print(age == 21)
print(age != 21)


#checking whether true or false for other data types like lists, strings, and numbers
print("\nchecking whether true or false for other data types like lists, strings, and numbers:")
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))



# IN CONDITIONAL STATEMENTS IF THE FIRST CHECK IS TRUE THEN THE REST OF THE CHECKS ARE NOT EXECUTED. 
# IF THE FIRST CHECK IS FALSE THEN THE NEXT CHECK IS EXECUTED AND SO ON UNTIL A TRUE CONDITION IS FOUND OR ALL CONDITIONS ARE CHECKED. 
# IF ALL CONDITIONS ARE FALSE THEN THE ELSE BLOCK IS EXECUTED IF PRESENT.
# THIS IS TRUE FOR IF, ELIF, AND ELSE CONDITIONALS AND THIS CHANGES WHEN INDENTATION CHANGES AND BECOMES NESTED LOOPS
#if conditionals
print("\nif conditionals:")
age = 21

if age >= 18:
    print("You are an adult.")


#else conditionals
print("\nelse conditionals:")
age = 16    

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


#elif conditionals
print("\nelif conditionals:")

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


#another example of elif conditionals
print("\nanother example of elif conditionals:")

marks = 82

if marks >= 40:
    print("Grade D")
elif marks >= 60:
    print("Grade C")
elif marks >= 75:
    print("Grade B")
elif marks >= 90:
    print("Grade A")



#multiple if statements
print("\nmultiple if statements:")  

temperature = 30

if temperature > 25:
    print("It's a hot day.")
if temperature > 20:
    print("It is above 20 degrees.")


#comparison operators
print("\ncomparison operators:\n")

print("*and* operator:")
age = 21
height = 175

if age >= 18 and height >= 160:
    print("You are eligible to apply.")
else:
    print("You are not eligible to apply.")


print("\n*or* operator:")
age = 16
height = 150

if age >= 18 or height >= 160:
    print("You are eligible to apply.")
else:
    print("You are not eligible to apply.")


print("\n*not* operator:")

age = 21

if not age < 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


#combining more than one comparison operator in a conditional statement using paranthesis
print("\ncombining more than one comparison operator in a conditional statement:")
has_license = True
age = 21
driving_experience = 1

if has_license and (age >= 18 or driving_experience >= 2):
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")



#Nested if statements
print("\nNested if statements:")

age = 21
has_license = False

if age >= 18:
    if has_license:
        print("Can drive under these criteria")
    else:
        print("License required")
else:
    print("Below the required age")



#Logical operators and Short circuit evaluation
#Here, the first condition is False, so the second condition is not evaluated and the result is False and 
#The second print statement evaluates to False because the first condition is True and the second condition is also False.
#So if the starting condition itself is False then the rest of the conditions are not evaluated and the result is False.
#For the third one the operator used is *or* which only requires anyone to be true so both are evaluated even though the second is False.
#For the Last example, the username is empty so it is False so the second condition is not evaluated and the result is False. If the username was not empty then the second condition would be evaluated and if it was True then the result would be True.
print("\nLogical operators and Short circuit evaluation:")

print(False and (10/2>4))
print(True and (10/2>6))
print(True or (10 / 2 > 6))

username = ""

if username and username[0] == "K":
    print("Username starts with K")
else:
    print("Username is empty or doesn't start with K")





