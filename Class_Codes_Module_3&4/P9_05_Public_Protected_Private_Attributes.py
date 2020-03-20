'''
Private, Public and Protected Attributes:
------------------------------------------
Private: Private attributes can only be accessed inside of the class definition.
Public: Public attributes can and should be freely used.
Protected: Protected attributes are accessible only from within the class and it's subclasses.
'''
#Example:
class Edureka_1():
    def __init__(self):
        self.__priv= "I am Private" #Private attribute with __(Double underscore)
        self._proc="I am Protected" #Protected attribute with _(Single underscore)
        self.publ="I am Public"     #Public attribute without underscore

ob=Edureka_1()
print(ob.publ)  #Accessing Public Attribute
print(ob._proc) #Accessing Protected Attribute
#print(ob.__priv)    #Accessing Private Attribute:  Throws AttributeError: 'Edureka_1' object has no attribute '__priv'
#So, only way to access Private attribute is with class name as below:
print(ob._Edureka_1__priv)  #I am Private
'''
O/P:
I am Public
I am Protected
AttributeError: 'Edureka_1' object has no attribute '__priv'
I am Private
'''
print(dir(ob))
'''
['_Edureka_1__priv', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_proc', 'publ']
'''
'''
Here we have _proc (Protected) as well as publ (Public) Attributes in object but not Private because private is listed with the class name(_Edureka_1__priv) 
'''
'''
Private Methods: When the attributes of an object can only be accessed inside the class, it is called a Private Class.
Python use "two underscores" to hide a Method. Two underscores can also be used to hide a Variable.
'''
class MyClass:
    def myPublicMethod(self):
        print("Public Method")
    def __myPrivateMethod(self):
        print("Private Method")

obj=MyClass()
obj.myPublicMethod()    #Public Method
#obj.__myPrivateMethod()    #AttributeError: 'MyClass' object has no attribute '__myPrivateMethod'
obj._MyClass__myPrivateMethod()     #Private Method: Private Methods can be accessed using One underscore("_") with class name.
'''
Output:
Public Method
Private Method
'''