class number:
    def __init__(self,num):
        self.num = num
    def large(self):
        a = max(self.num)
        return a
    
m= list(map(int, input('Enter two number:\n').rstrip().split()))
lg =  number(m)
print('Largest number is:',lg.large())