#Constructor and Destructor
'''
Construtor: __init__(self) is initiation method for any class. This is also called as contructor
Destructor: It is executed when we destroy any object or instance of the class. __del__(self) is destructor method for destrying the object.
'''
class TestClass:
    def __init__(self):     #The constructor is implemented using __init__(self) which you can define parameters that follows itself.
        print("constructor")
    def __del__(self):      #The destrutor is defined using __del__(self). In the example, the obj is created and manually deleted, therefore
        print("destructor") #both messages will be displayed.

if __name__=="__main__":
    obj=TestClass()
    del obj
'''
O/P:
constructor
destructor
'''
#Multiple Constructors:
#----------------------#
class Date:
    def __init__(self, year, month, day):   #Year-Month-Day
        self.Year=year
        self.Month=month
        self.Day=day
        print("Constructor Initialization")
    @classmethod        #Constructors
    def dmy(self, day, month, year):    #Day-Month-Year
        self.Year=year
        self.Month=month
        self.Day=day
        return self(self.Year, self.Month, self.Day)    #order of return should be same as __init__
    @classmethod        #Constructors
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