import math
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = (b * b) - (4 * a * c)
if(d > 0):
    root1 = (-b + math.sqrt(d) / (2 * a))
    root2 = (-b - math.sqrt(d)/ (2 * a))
    print("Two distinct real roots exists: root1=",root1 ,"and root2 =" , root2)
elif(d == 0):
    root1 = root2 = -b / (2 * a)
    print("Two equal and real roots exists: root1=",root1 ,"and root2 =" , root2)
elif(d < 0):
    root1 = root2 = -b / (2 * a)
    i = math.sqrt(-d) / (2 * a)
    print("Two distinct complex roots exists: root1 =",root1,"+",i,"and", "root2 =",root2,"-",i)
