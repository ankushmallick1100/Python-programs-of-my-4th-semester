x = int(input('Enter first number:'))
y = int(input('Enter second number:'))
a = lambda x,y:min(x,y)
print('Smallest number is:',a(x,y))