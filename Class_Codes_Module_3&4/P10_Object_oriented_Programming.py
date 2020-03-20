#Object Oriented Programming:
#----------------------------#
'''
Object Oriented Programming Paradigm is very popular and very useful in nature.
Object-Oriented-Programming: Key Concepts: There are basically 5 properties of OOPs that is why it is preferred over POP:
#------------------------------------------#----------------------------------------#
--> Abstraction
--> Encapsulation
--> Inheritance
--> Overriding
--> Polymorphism
#------------------------------------------#
'''
###############################################"*****Abstraction*****"#############################################################
#Abstraction:
'''
#-----------#
--> Abstraction is simplifying complex reality by modelling classes appropriate to the problem.
--> Class abstraction means to separate class implementation from the use of the class.
'''
#Example:
class Date:
    def __init__(self, year, month, day):   #Year-Month-Day
        self.Year=year
        self.Month=month
        self.Day=day
        print("Constructor Initialization")
    @classmethod        #Constructors due to fun+return statement
    def dmy(self, day, month, year):    #Day-Month-Year
        self.Year=year
        self.Month=month
        self.Day=day
        return self(self.Year, self.Month, self.Day)    #order of return should be same as __init__
    @classmethod        #Constructors due to fun+return statement
    def mdy(self, month, day, year):    #Month-Day-Year
        self.Year=year
        self.Month=month
        self.Day=day 
        return self(self.Year, self.Month, self.Day)    #order of return should be same as __init__

a=Date(2016,8,19)       #Constructor Initialization
print(a.Year)           #2016
b=Date.dmy(4,8,1995)    #Constructor Initialization
print(b.Year)           #1995
c=Date.mdy(11,9,1998)   #Constructor Initialization
print(c.Year)           #1998

'''
Here in this example, So, much of complex processing has been done for Date class but we use it in a very simple way and create an object. When we use the
object, we never go back to the code and never worry about what has been written inside the class. This property of separating the inside working of a 
class from it's instance by creating this concept of class is known as abstraction.
'''
###############################################"*****Encapsulation*****"#############################################################
#Encapsulation:
#--------------#
'''
Encapsulation: 
--> Combining the code into a public Interface, and a private implementation of that interface.
--> It is a mechanism for restrcting the access to some of an objects component, which means that the internal representation
of an object can not be seen from outside of the objects definition.

So, as per our previous example, We only use the public interface which is object implementation(like a, b, c) and the code is generally private 
implementation not in the public domain.
'''
###############################################"*****Inheritance*****"#############################################################
#Inheritance:
#------------#
'''
Inheritance:
--> Inheritance is the powerful feature of Object Oriented Programming.
--> It refers to deriving a class from the base class with little or no modification in it.

-->Types of Inheritance:
#-------------------------#
######################################
Single Inheritance: Derived Class is inheriting properties from 1 Base class
-------------------
A<------Base Class
|
|
|
B<------Derived Class
#######################################
Multiple Inheritance: Derived Class is inherting properties from 2 or more Base classes
----------------------
A           B<----Base Class
|           |
|           |
-------------
    |
    |
    C   <-----Derived Class
########################################
Multilevel Inheritance: Derived Class is inherting properties from another derived class which is inherting from another base class
------------------------
A<---Base Class
|
|
B<---Derived Class from A
|
|
C<---Derived Class from B
##########################################
'''
###Single Inheritance:
#-------------------#
'''
Single Inheritance: Derived Class is inheriting properties from 1 Base class
-------------------
A<------Base Class
|
|
|
B<------Derived Class

--> Important benefits of inheritance are code reuse and reduction in the complexity of a program
'''
#Example: Single Inhertance:
class Base:
    def __init__(self):
        print("Base Constructor")
    def fun(self):
        print("Base class fun")

class Derived(Base):
    def __init__(self):
        print("Derived Constructor")
        pass
ob=Derived()    #def fun function from base class is inherted in derived class and derived class can access the method inside that funtion.
ob.fun()
'''
O/P:
Derived Constructor
Base class fun
'''
###Multiple Inheritance:
#-----------------------#
'''
Multiple Inheritance: Derived Class is inherting properties from 2 or more than 2 Base classes
----------------------
A<Base 1    B<----Base2 Class
|           |
|           |
-------------
    |
    |
    C   <-----Derived Class
(Features of Base1 class + Base2 class + multiderived Class)

'''
#Example: Multiple Inheritance:
class First:
    def __init__(self):
        print("Base class 1 constructor")
        super(First, self).__init__()
        print("First")

class Second:
    def __init__(self):
        print("Base class 2 constructor")
        super(Second, self).__init__()
        print("Second")

class Third(First,Second):
    def __init__(self):
        print("Derived class constructor")
        super(Third, self).__init__()
        print("Third")

Third()
'''
O/P:
Derived class constructor
Base class 1 constructor
Base class 2 constructor
Second
First
Third
'''

###Multilevel Inheritance:
#-------------------------#
'''
A<---Base Class
|
|
B<---Derived Class from A
|
|
C<---Derived Class from B
'''
#Example: Multilevel Inheritance:
class Animal:
    def eat(self):
        print("Eating....")

class Dog(Animal):
    def bark(Self):
        print("Barking....")

class Puppy(Dog):
    def weep(self):
        print("Weeping....")

tommy=Puppy()
tommy.eat()
tommy.bark()
tommy.weep()
'''
O/P:
Eating....
Barking....
Weeping....
'''
###############################################"*****Overriding*****"#############################################################
#Overriding:
'''
Base class methods can always be overrided. One reason for overriding Base's methods is because you may want special or different functionality
in your derived class.
'''
#Example:
class Base:
    def fun(self):
        print("Base class fun function")

class Derived:
    def fun(self):
        print("Derived class fun function")

d=Derived()
d.fun()
'''
O/P:
Derived class fun function

Derived class overrides the method or function written in Base class.
'''
###############################################"*****Polymorphism*****"#############################################################
#Polymorphism:
#-------------#
'''
Polymorphism: Polymorphism is the ability to leverage the same interface for different underlying forms such as data types or classes.
--> Polymorphism is an important feature of class definition in Python that is utilized when you have commonly named methods across classes or
subclasses.
'''
#Example:
class Animal:
    def __init__(self, name):
        self.name=name
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(Self):
        print("bark")

c=Cat()
c.talk()
d=Dog()
d.talk()