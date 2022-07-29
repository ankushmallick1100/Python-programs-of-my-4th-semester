def sorted(a):
    f = 0
    for i in range(0,len(a)-1):
        if(a[i]>a[i+1]):
            f = 1
            break
    if f == 1:
        return False
    else:
        return True