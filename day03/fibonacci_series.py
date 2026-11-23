def fibonacci(n):

   a=0
   b=1
   if n > 0 and n!=1:
     
       print(a,b,end=" ")
       for i in range(0,n-2):
        a,b = b, a+b
        fib = b
        print(fib, end=" ")

   elif n == 1:
      print(a)

   else:
       print("Enter a limit greater than 0")

n = int(input("Enter upto where the fibonacci sequence needs to be printed:"))
fibonacci(n)


