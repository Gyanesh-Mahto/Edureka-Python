'''
For Loop: "For" Loop is a python loop which repeats a group of statements as specified number of times.
The for loop provides a syntax where the following information is provided:
-Boolean condition
-The initial value of the counting variable
-Incrementing of counting variable

Syntax:
for <variable> in <range>:
    statement 1
    statement 2
    statement 3
    ...........
    statement n
'''

'''
Q] What is the difference between a for loop and while loop?
Sol: The only difference between for loop and while loop is that, in while loop we don't know the amount of iterations, where as in
For loop we are aware of how many times the block of code will be executed.
'''
'''
range function: It is an inbuilt function in python which will create a range of values.

syntax:
range(start, stop, step)    <---But giving all three arguments are not necessary
range(start, stop)  <--Here start is inclusive, stop is exclusive(n-1) or (stop-1)
range(stop)
'''
print(list(range(0, 10, 2)))        #range(start, stop, step)
#O/P:
#[0,2,4,6,8]

print(list(range(0, 10, 1)))        ##range(start, stop, step)
#O/P:
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(4, 10)))           #range(start, stop)
#O/P:
#[4, 5, 6, 7, 8, 9]

print(list(range(10)))              #range(stop)
#O/P:
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
for loop example:
'''
m_name_list=['Anubhav', 'Yuyutsu', 'Abhijeet', 'Ranvijay', 'Gyanesh', 'Manoj']
f_name_list=['Vimmi', 'Ruchi', 'Kusum', 'Pooja', 'Hithaishi', 'Riya']

for num in range(len(m_name_list)):
    print(m_name_list[num])

#O/P:
#Anubhav
#Yuyutsu
#Abhijeet
#Ranvijay
#Gyanesh
#Manoj

for name in m_name_list:        #Another way of for loop
    print(name)

#O/P:
#Anubhav
#Yuyutsu
#Abhijeet
#Ranvijay
#Gyanesh
#Manoj