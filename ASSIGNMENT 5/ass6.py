import re
def removevol(a):
    return (re.sub("[aeiouAEIOU]","",a))

a = input('Enter a string:\n')
print(removevol(a))