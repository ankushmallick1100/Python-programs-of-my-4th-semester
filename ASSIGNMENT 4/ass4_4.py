def leapyear(a):
    if(a%4==0):
        if(a%100==0):
            if(a%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

a = int(input("Enter a number:"))
if(leapyear(a)):
    print(a," is Leap Year")
else:
    print(a," is not a Leap Year")
