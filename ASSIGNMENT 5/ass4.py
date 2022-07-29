a = input("Enter a string : ")
i = 0
print('Encrypted string is:')
for item in a:
    b = ord(a[i])
    b += 3
    c = chr(b)
    print(c," ")
    i+=1
