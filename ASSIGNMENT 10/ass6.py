a = [[1,0,0],[2,0,0],[3,0,0]]
dict = {}
for i in range(len(a)):
	for j in range(len(a[i])):
		if a[i][j] != 0:
			dict[i, j] = a[i][j]
print(dict)