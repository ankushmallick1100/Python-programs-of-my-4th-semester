x = input("Enter user's name:")
y = input('Enter pan card number:')
if(x.isalpha() and y.isalnum()):
    print('This two informations are valid')
else:
    print('This two informations are not valid')


