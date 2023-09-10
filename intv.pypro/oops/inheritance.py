# Inheritance

class Person(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is an employee
    def isEmployee(self):
        return False
 

 # Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True
    

# Driver code
# per = Person("Rabi")  # An Object of Person
# print(per.getName())
# print(per.isEmployee(), '\n')

# emp = Employee("Kishan")
# print(emp.getName())
# print(emp.isEmployee(3))




# parent class
class Persons():
  local = 'Hello Local'
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Persons):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", 17)
    super().display()
    print(super().local)
    print('....')
 
  def displayInfo(self):
    print(self.sName, self.sAge)
    print('---')
    super().__init__("Gyana", 54)
    super().display()
 
obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

