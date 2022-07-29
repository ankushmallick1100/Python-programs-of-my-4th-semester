x=int(input("Enter a number: "))
y=int(input("Enter exponential value: "))
res=1
for i in range(1,y+1):
    res= res * x
print("Result is:",res)