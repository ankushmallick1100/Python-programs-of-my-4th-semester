import math
def isArmstrong(n):
    l = len(n)
    n = int(n)
    a = n
    s = 0
    while(n!=0):
        r = n%10
        s += math.pow(r,l)
        n = n//10
    
    if(a == s):
        return True
    else:
        return False
