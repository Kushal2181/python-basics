#My approach and the bug it caused was for n = 0 it prints nothing

def fibonacci(n):

   a=0
   b=1
     
   for _ in range(n-1):
    a,b = b, a+b

   return b
        
n = int(input("Enter upto where the fibonacci sequence needs to be printed:"))
print(fibonacci(n))


#Corrected approach

def fibonacci(n):

   a=0
   b=1
     
   for _ in range(n):
    a,b = b, a+b

   return a
        
n = int(input("Enter upto where the fibonacci sequence needs to be printed:"))
print(fibonacci(n))