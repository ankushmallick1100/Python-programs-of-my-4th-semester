a = input("Enter a string : ")
b = input("Enter the character : ")
i = 0
c = 0
while(i < len(a)):
    if(a[i] == b):
        c += 1
    i = i + 1
print('The occurence of a character is',c)