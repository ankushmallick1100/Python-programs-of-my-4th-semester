num = int(input("Enter a number: "))
sum = 0
a = num
while a > 0:
   dig = a % 10
   sum += dig ** 3
   a //= 10
if num == sum:
   print('It is an Armstrong number')
else:
   print('It is not an Armstrong number')