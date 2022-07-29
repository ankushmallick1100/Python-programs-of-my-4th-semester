List = [10, 20, 30, 40, 50]
temp = List[0]
List[0] = List[1]
List[1] = temp
print('List after swapping two elements is:',List)