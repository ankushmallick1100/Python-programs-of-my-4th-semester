n= int(input("Enter number of terms:"))
a=0
b=1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto 1 term is:",a)
else:
   print("Fibonacci sequence of", n,"terms is:")
   while count < n:
       print(a)
       d = a + b
       a = b
       b = d
       count = count + 1