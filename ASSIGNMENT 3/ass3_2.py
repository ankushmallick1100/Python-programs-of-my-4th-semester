a =int(input('Enter a number:'))
fact = 1
sum = 0    
for i in range(1,  a+1):
    fact = fact * i
    sum = sum + (i/ fact)   
print("Solution of the given series is:",sum)