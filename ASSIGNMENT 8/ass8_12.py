List = [10, -11, -12, 13, -14, 15, 16]
positive = 0
negative = 0
for i in List:
	if i >= 0:
		positive = positive + 1
	else:
		negative = negative + 1	
print("Positive numbers in that list is: ", positive)
print("Negative numbers in that list is: ", negative)