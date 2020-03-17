#Example_1
'''
class Edureka():
    def Hello(self):
        print("Happy Learning")

ob=Edureka()
ob.Hello()

#O/P:
#Happy Learning
'''
#Example_2:
'''
class Edureka():
    def __init__(self, location):   #When any variable or object is created then init function will be invoked for that particular object or variable.
        self.location=location
    def print_1(self):
        print("This object belongs to location: {}".format(self.location))

new_loc_1=Edureka("Delhi")
new_loc_1.print_1()             #This object belongs to location: Delhi
new_loc_2=Edureka("Patna")
new_loc_2.print_1()             #This object belongs to location: Patna
print(type(new_loc_1))          #<class '__main__.Edureka'>: Here object data type is class "Edureka"
print(type(new_loc_2))          #<class '__main__.Edureka'>
print(dir(Edureka))             ##Attributes and inbuilt function of class
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'print_1']
'''
print(dir(new_loc_1))       #Attributes and inbuilt function of object
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__', 'location', 'print_1']
'''
print(new_loc_1.location)       #Delhi : Using attribute "location" available in new_loc_1
print(new_loc_2.location)       #Patna  : Using attribute "location" available in new_loc_2
'''
##What is the significance of self?
#Self signifies that the function needs to be initated for the particular object and not on all objects of the class.
'''
NOTE: A function in a class can't be defined as def fun() <---without self argument, it will throw error as fun() takes 0 positional argument but 1 was
given. That's why we should always define fun in a class with self keyword.
#def fun(self)
'''
'''
NOTE: Here __init__() is declared explicitely in class because argument "location" was passed in the class. If no argument is passed in the class, then,
explicit declaration of __init__() is not required.
'''
#Example: 3
class Edureka():
  #  def __init__(self, location):   #When any variable or object is created then init function will be invoked for that particular object or variable.
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
NOTE: Here self is mandatory. self should always be the first parameter.
'''
