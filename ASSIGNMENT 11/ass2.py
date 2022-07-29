class circle:
    def __init__(self,rad):
        self.rad = rad
    def area(self):
        print(3.14*self.rad*self.rad)
    def circumference(self):
        print(2*3.14*self.rad)

obj1 = circle(10)
obj1.area()
obj1.circumference()
