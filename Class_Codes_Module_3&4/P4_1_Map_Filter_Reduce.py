#map:
'''
-> map applies a function to all the items in an input_list.
-> Map will give you as many output or the return of map will be as many number of elements 
present in list.
'''

#filter:
'''
-> As the name suggests, filter creates a list of element for which a function returns true.
->filter will give you lesser number of output or the return of filter will ne less than the
number of elements present in list.
'''

#reduce:
'''
-> reduce is really useful function for performing some computation on a list and returning the
result.
-> reduce will return a single value.
'''

#Examples:
#---------#
#map:
items=[1,2,3,4,5]
sqaured=list(map(lambda x:x*2, items))
print(sqaured) 
#O/P: [2, 4, 6, 8, 10]

#filter:
number_list=range(-5, 5)
less_than_zero=list(filter(lambda x: x<0, number_list))
print(less_than_zero)
#O/P: [-5, -4, -3, -2, -1]

#reduce:
from functools import reduce    #reduce function is present in functools
product=reduce((lambda x, y:x*y),[1,2,3,4])
print(product)
#24
###################################################################################333
#Even numbers between 1 to 50
numbers=range(1,50)
even=list(filter(lambda x: x%2==0, numbers))
print(even)
#O/P:
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

