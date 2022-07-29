List = [10, 20, 30, 40, 50]
print('List before interchanging:',List)
Length = len(List)
temp = List[0]
List[0] = List[Length - 1]
List[Length - 1] = temp
print('List after interchanging the first and last element is:',List)