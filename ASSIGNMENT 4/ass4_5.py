def fibonacci(n):
    if n<= 1 :
      return n
    else :
      return(fibonacci(n-1) + fibonacci(n-2))

terms = 8

if terms<= 0:
    print("Please enter a positive number")
else: 
    print("Fibonacci Sequence")
for i in range(terms):
   print(fibonacci(i))