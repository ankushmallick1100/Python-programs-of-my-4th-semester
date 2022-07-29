class GrandParent: 
  def __init__(self):
    print("I am a GrandParent Class")

class Parent(GrandParent):
  def __init__(self):
    print("I am  a Parent Class. Derived from Grandparent class")

class Children(Parent, GrandParent): 
  def __init__(self):
    print("I am a Children class. Derived from GrandParent and Parent classes")

obj1 = GrandParent()
obj2 = Parent()
obj3 = Children()