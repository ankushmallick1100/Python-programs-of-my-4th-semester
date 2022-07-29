str = input('Enter a string:')
vol = ['a','e','i','o','u']
res = [letter for letter in str if letter.lower() not in vol]
res = ''.join(res)
print(res)
 
