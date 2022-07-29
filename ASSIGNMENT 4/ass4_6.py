def binarytodecimal(n):
  i,res=0,0
  while(n!=0):
    rem = n%10
    res = res + rem*pow(2,i)
    n = n//10
    i+=1
  print(res)

def decimaltobinary(n1):
  if(n1>1):
    decimaltobinary(n1//2)
  print(n1%2, end= " ")
n = int(input("Enter the binary digit: "))
n1 = int(input("Enter the decimal number: "))
binarytodecimal(n)
decimaltobinary(n1)