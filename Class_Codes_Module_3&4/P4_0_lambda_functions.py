'''
Normal Function:
In normal function, first we have to define a function, then we need to call that function, then
we will get result.
But sometime, we need a function which we will use only once. There will be many
scnarios where we need to use a function only once. For that we have Lambda Functions.
'''
#Lambda Functions:
'''
-In case you wish to make your functions more concise, easy to write and read, you can create 
lamda functions.
-Anonymous Lambda function can be defined using the keyword: lambda
-Lambda functions cannot contain commands, and they can not contain more than one expression.
-Lambda function can take any number of arguments(including optional arguments) and returns the
value of a single expression.
'''
#example:
ans=(lambda z:z*4)
print(ans(7))       #28

'''
--> While normal functions are defined using def keyword, In python, anonymous functions are defined
using lambda keyword.
--> We can use Lambda function when we require a nameless function for short period of time.
'''
#Square values of numbers from 0 to 100:
list1=list(range(0,101))
print(list1)
#[0,1,2,3,....,97,98,99,100]
print(list(map(lambda x:x**2, list1)))  #By suing lambda function, consice code is written.
#[0,1,4,9,...,9409, 9604, 9801, 10000]

#Lambda on list of strings
list2=['Apple', 'Banana', 'oranges', 'grapes']
print(list2)
#['Apple', 'Banana', 'oranges', 'grapes']
print(list(map(lambda x:x.capitalize(), list2)))
#['Apple', 'Banana', 'Oranges', 'Grapes']
print(list(map(lambda x:x.upper(), list2)))
#['APPLE', 'BANANA', 'ORANGES', 'GRAPES']


