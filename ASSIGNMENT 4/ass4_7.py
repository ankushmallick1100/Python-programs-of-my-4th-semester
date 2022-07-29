def power(base,exponent):
    if(exponent==1):
        return(base)
    if(exponent!=1):
        return(base*power(base,exponent-1))
base=int(input("Enter base value:"))
exponent=int(input("Enter exponential value:"))
print("Result:",power(base,exponent))