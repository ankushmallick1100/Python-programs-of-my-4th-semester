l=int(input("Enter the length of cuboid: "))
b=int(input("Enter the breadth of cuboid: "))
h=int(input("Enter the height of cuboid: "))
if(l<0 or b<0 or h<0) :
    print("Parameters can't be negavite values")
else :
    vol= l * b * h
    print("The volume of the cuboid is : ",vol)