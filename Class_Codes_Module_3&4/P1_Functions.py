'''
Why do we need functions?
-> When we have some activity which we have to do repeatedly, Then in this scenario, we write
functions and call that function again and again.
-> 
'''
'''
#Factorial of a number:
n=int(input("Please enter any number: "))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)
'''
'''
#Factorial function:
def fn_fact(n):     #Function Definition
    i=1
    fact=1
    while i<=n:
        fact=fact*i
        i+=1
    return(fact)

n=int(input("Please enter any number: "))
facto=fn_fact(n)
print(facto)
'''
'''
Advantage of return(): It will return the value from function which can be used to take value.
Multiple values can also be returned from return() as can be seen with below example:
'''

#Factorial function:
def fn_fact(n1):     #Function Definition
    i=1
    fact=1
    while i<=n1:
        fact=fact*i
        i+=1
    return(fact, fact**2)

n1=int(input("Please enter any number: "))
facto, sqr_fact=fn_fact(n1)
print("Factorial of {} is {} and square of factorial is {}".format(n1, facto, sqr_fact))
#O/P:
#Please enter any number: 6
#Factorial of 6 is 720 and square of factorial is 518400

##############################################################################################

#Function Definition and Function Call:
'''
#Function Definition: The set of statements written once executed multiple times.
#def is the keyword for defining the function.
#Function Call: Once we define the Function, we can call it multiple times.
We can pass same number of arguments in function call which is defined in function call.
def print_name(str):        #Function Definition
    print("Wecome to Edureka, ", str)
    return()

str=input("Please enter your name:")
print_name(str)         #Function Call
'''
##Why use the return statement?
#The return statement terminates the execution of a function and return control to the calling
#function
