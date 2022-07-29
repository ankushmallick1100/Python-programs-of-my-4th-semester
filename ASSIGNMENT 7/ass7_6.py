import sort
n =int(input("Enter the number of elements: "))
a = []
for i in range(0,n):
    ele = int(input(f"Enter Element {i}: "))
    a.append(ele)

if(sort.sorted(a)):
    print("Sorted")
else:
    print("Not Sorted")
