import re
list = ["Apple", "Banana", "Orange"]
for element in list:
    z = re.match("(g\w+)\W(g\w+)", element)
if z:
    print((z.groups()))
    
text = 'Apple and Orange are very tasty.'
for item in list:
    print('Looking for "%s" in "%s" ->' % (item, list))
    if re.search(item, text):
        print('Found a match.')
    else:
        print('No match.')

s = "The sun rises in the East."
res_1 = re.sub('in', 'ab', s)
print(s)
print(res_1)


abc = 'apple@gmail.com, banana@gmail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for i in emails:
    print(i)