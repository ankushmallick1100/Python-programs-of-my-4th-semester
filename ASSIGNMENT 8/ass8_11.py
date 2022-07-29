List = [10, 11, 12, 13, 14, 15, 16]
even = 0
odd = 0
for i in List:
	if i % 2 == 0:
		even = even + 1
	else:
		odd = odd + 1	
print("Even numbers in that list is: ", even)
print("Odd numbers in that list is: ", odd)