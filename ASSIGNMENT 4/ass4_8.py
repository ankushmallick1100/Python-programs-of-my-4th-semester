def palindrome(n):
    rev = 0
    rem = 0
    while(n!=0):
        rem = n % 10
        rev = rev * 10 + rem
        n = int (n/10)
    return rev

num = int(input("Enter the number:"))
rev = palindrome(num)
if(num == rev):
    print(num," is a palindrome")
else:
    print(num," is not a palindrome")