'''
-->Attributes:
->Class attributes are attributes which are owned by the class itself. They will be shared by all the instances of the class.
->There are two types of Attributes:
1. Built-in Attributes.
2. User Defined Attributes.
'''
#Example:
#Example: 3
class Edureka():
  #  def __init__(self, location):   #When any variable or object is created then init function will be invoked for that particular object or variable for initialisation.
  #      self.location=location
    def set_location(self, loc):
        #self.location=input("Please enter your location: ")    #It also works fine
        self.location=loc   #The special thing about this function is in the name, as it is being used to set a particular value for class vaiable.
    def print_1(self):      #The above method for setting the value is called "setter" method
        print("This object belongs to location: {}".format(self.location))  #This method of getting a value is called "Getter" method.

new_loc_1=Edureka()
new_loc_1.set_location("Delhi")        #Please enter your location: Delhi
new_loc_1.print_1()             
new_loc_2=Edureka()
new_loc_2.set_location("Patna")       
new_loc_2.print_1()             #This object belongs to location: Patna

'''
--->Here in "def set_location(self,loc), self.location" location is "User-Defined attribute" which we can see by dir(new_loc_1) available for Edureka class. 
But apart from this there are inbuilt attributes also available for Edureka class.
'''
print(dir(new_loc_1))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'location', 'print_1', 'set_location']
'''
'''
So, Here "location" is attribute and "print_1, set_location" are function.
location--->User-Defined attribute
set_location, print_1--->Function
'''
'''
IMPORTANT: 
===>what is method and function in python?
-->A method commonly refers to a function that's a property of a class (either a static or instance method), 
while a function is the more general term for a procedure that takes arguments and returns a value after being called. Methods are functions.

===>What is the difference between attributes and methods in Python?
-->A variable stored in an instance or class is called an attribute.
-->A function stored in an instance or class is called a method.

-->Attribute:
A value associated with an object which is referenced by name using dotted expressions. 
For example, if an object o has an attribute a it would be referenced as o.a

-->Method:
 A function which is defined inside a class body. If called as an attribute of an instance of that class, 
 the method will get the instance object as its first argument (which is usually called self). See function and nested scope.
'''
'''
Some In-built attributes:
'''
print(new_loc_1.__dict__)   #__dict__ attribute will return the value of each and evry attribute present inside the class.
#{'location': 'Delhi'}
print(new_loc_2.__dict__)
#{'location': 'Patna'}
print(new_loc_1.__dir__)    #It will return the class name of object prvided
#<built-in method __dir__ of Edureka object at 0x0175F6F0>