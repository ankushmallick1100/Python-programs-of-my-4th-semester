a = input("Enter a string : ")
b = input("Enter the character : ")
i = 0
while(i < len(a)):
    if(a[i] == b):
        c = a.index(b)
    i = i + 1
print(f'{b} is present in the string at index no {c}')