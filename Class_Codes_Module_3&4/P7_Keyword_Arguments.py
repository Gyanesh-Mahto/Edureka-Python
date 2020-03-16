#Keyword Arguments:
'''
-> When keyword arguments are used in a function call, the caller identifies the arguments by the
parameter name.
'''

def add_emp(name, age): #The arguments provided here are called as named arguments.
    print("{}\'s age is {}".format(name, age))

add_emp("Anumbhav", 30)

#Anumbhav's age is 30

'''
NOTE:For Named Arguments, sequence is very important:
'''
add_emp(30, "Anumbhav")
#30's age is Anumbhav

'''
Keyword Arguments:
'''
def Welcome(str1):
    print("Welcome to python, ", str1)
    return()

Welcome(str1="Anubhav")
#O/P: Welcome to python,  Anubhav
#Here, String is passed as an argument when the function is called.
add_emp(age=25, name="Sakshi")
#Sakshi's age is 25

'''
Default Arguments: 
-> A default argument is an argument that assumes a default value if a value is not provided in
the function call for that argument.
-> It signifies that it is not necessary to give a value during function call, the default value
provided in function argument is taken
'''
def add_emp1(name, age, id1=100):
    print("{}\'s age is {} and his/her employee id is".format(name, age), end=' ')
    print(id1)

add_emp1(name="Yuyutsu", age=30, id1=20)    #Keyword Arguments
#O/P: Yuyutsu's age is 30 and his/her employee id is 20
add_emp1(name="Bhanu", age=300)             #Default Argument
#O/P: Bhanu's age is 300 and his/her employee id is 100