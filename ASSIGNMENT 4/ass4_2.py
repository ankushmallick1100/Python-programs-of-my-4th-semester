a = int(input("Enter a number:"))
def factorial(a):
    fact = 1
    if(a==1):
        return 1
    return a*factorial(a-1)
    
print("The factorial is ",factorial(a))