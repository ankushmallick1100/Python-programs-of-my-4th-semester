class student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        print('Students Name is:',self.name)
        print('Marks of subhject1 is:',self.marks1)
        print('Marks of subhject2 is:',self.marks2)
        print('Marks of subhject3 is:',self.marks3)

    def average(self):
        print('Aveage of three subjects is:',(self.marks1+self.marks2+self.marks3)/3)
    
obj = student('Ankush',10,20,30)
obj.display()
obj.average()