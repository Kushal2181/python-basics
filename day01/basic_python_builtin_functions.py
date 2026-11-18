print("storing data(words) in a variable and printing the variable:\n")
message = 'Hello World'
print(message) 

#printing a variable that is stored in single quotes '' but we have another single quote in data for proper grammer so used \ to make the program understand that the single quote is also part of the words or data 
print("\nprinting a variable that is stored in single quotes '' but we have another single quote in data for proper grammer so used \"\\\" to make the program understand that the single quote is also part of the words or data: ")
message_2nd = 'Kushal\'s world'
print(message_2nd)

#printing a variable stored in between double quotes "" this is an alternative for not using any '\' like above
print("\nprinting a variable stored in between double quotes this is an alternative for not using any '\\' like above:")
message_3rd = "Kushal's world"
print(message_3rd)

#storing multiple lines or sentences in a single variable using triple quotes """ and printing it
print("\nstoring multiple lines or sentences in a single variable using triple quotes and printing it:")
message_4th = """The country with most population is India
and the economy of India is steadily growing
by 6-7 percent every year"""
print(message_4th)


#printing the length or no of characters of data that is stored in variable
print("\nprinting the length or no of characters of data that is stored in variable:")
print(len(message_4th))


#turning all the data in the variable into lower case characters
print("\nTurning all the data in the variable into lower case characters:")
print(message.lower())

#turning all the data in the variable into upper case characters
print("\nTurning all the data in the variable into upper case characters:")
print(message.upper())

#capitalize a word
print("\nCapitalizing a word:")
print(message.capitalize())

#title-case a sentence
print("\nTitle-casing a sentence:")
sentence = '''himalayas are the tallest mountains in the world'''
new_sentence = sentence.title()
print(f"Title case of the sentence is: {new_sentence}")

#swapping the case of the data stored in the variable
print("\nSwapping the case of the data stored in the variable:")
print(message.swapcase())

#removing the white spaces in the data stored in the variable
message_2nd = '   Hello World   '
print("\nRemoving the white spaces in the data stored in the variable:")
print(message_2nd.strip())

#removing the white spaces in the data stored in the variable but only from the left side
print("\nRemoving the white spaces in the data stored in the variable but only from the left side:")
print(message_2nd.lstrip()) 

#removing the white spaces in the data stored in the variable but only from the right side
print("\nRemoving the white spaces in the data stored in the variable but only from the right side:")
print(message_2nd.rstrip()) 

#counting how many times the specified character or element is repeating in the data in the variable
print("\nCounting how many times the specified character or element is repeating in the data in the variable:")
print(message.count('l'))

#counting how many times the specified word or group of characters is repeating in the data in the variable
print("\nCounting how many times the specified word or group of characters is repeating in the data in the variable:")
apple = "Mango, banana, grapes, Mango, pine, Mango, Mango"
pie = apple.count('Mango')
print(pie)

#finding or locating if the specified word is actually present in the varaible
print("\nFinding or locating if the specified word is actually present in the variable:")
print('Hello' in message)

#finding the index of the specified word in the varaible
print("\nFinding or locating if the specified word is actually present in the variable:")
print(message.find('Hello'))

#finding or locating if the specified word is actually present in the varaible but if it is not present then it will return -1
print("\nFinding or locating if the specified word is actually present in the variable but if it is not present then it will return -1:")
print(message.find('Earth'))

#finding the index of the specified word in the variable
print("\nFinding the index of the specified word in the variable:") 
print(message.index('World'))


#replacing the data stored in the variable with another specified data
print("\nReplacing the data stored in the variable with another specified data:")
message_5th = message.replace('World','Earth')
print(message_5th)

#replacing the data stored in the variable with another specified data but only for the first 2 occurrences
#The number specifies how many times the specified data is to be replaced in the variable
print("\nReplacing the data stored in the variable with another specified data but only for the first 2 occurrences:")
message_5th = apple.replace('Mango','Apple',1)
print(message_5th)

#splitting the data stored in the variable into a list of words using split function
print("\nSplitting the data stored in the variable into a list of words using split function:")
message_6th = message.split()
print(message_6th)
print(message_6th[0])
print(len(message_6th))

#joinning the string which is separated into a list of words using join function
print("\nJoining the string which is separated into a list of words using join function:")
print(" ".join(message_6th))
print("-".join(message_6th))
print(".".join(message_6th))


#performing operations like sum and division
print("\nPerforming operations like sum and division:")
m1= 45
m2= 34
m3= 56
m4= 68
m5= 98
m6= -45
total = m1+m2+m3+m4+m5
print("Sum:",total)
average = total/5
print("Average:",average)
income=40000
expense=25000
savings=income-expense
print("My monthly savings are :",savings)


#finding absolute value and value rounded to nearest digit using func
print("\nFinding absolute value and value rounded to nearest digit using func:")
print(abs(total))
print(round(average))
print(abs(m6))


#finding the types of data using type func
name = "Kushal"
age = 21
height = 5.11
print("\nFinding the types of data using type func:")
print(type(name),type(age),type(height))