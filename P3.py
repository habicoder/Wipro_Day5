# START Procedure Fibonacci(n)   declare f0, f1, fib, loop        set f0 to 0   set f1 to 1       display f0, f1        for loop ← 1 to n           fib ← f0 + f1          f0 ← f1       f1 ← fib       display fib    end for END

#Python code for fibonacci Series
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  