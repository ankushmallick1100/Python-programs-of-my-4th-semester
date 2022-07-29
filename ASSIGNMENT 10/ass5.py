def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
dic = {}
a=int(input("Enter the value of n:"))
for i in range(a+1):
    dic[i] = fibo(i)
print(dic)