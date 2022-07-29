class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def display_data(self):
    print("Name : ",self.name)
    print("Age: ",self.age)
class Teacher(person):
  def __init__(self,name,age,exp,research_area):
    person.__init__(self,name,age)
    self.exp = exp
    self.research_area = research_area
  def display_data(self):
    person.display_data(self)
    print("Experience: ",self.exp)
    print("Research area: ",self.research_area)
class Student(person):
  def __init__(self,name,age,course,marks):
    person.__init__(self,name,age)
    self.course = course
    self.marks = marks
  def display_data(self):
    person.display_data(self)
    print("course: ",self.course)
    print("Marks ",self.marks)

obj = Teacher("Sanjay Chakraborty",40,15,"Data Science")
obj.display_data()
obj = Student("Ankush Mallick",21,"B.Tech, CSE",9.23)
obj.display_data()