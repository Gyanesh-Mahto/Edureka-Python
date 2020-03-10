'''
While loop: "While" loops are known as indefinite or conditional loops. They will keep iterating until certain conditions are met.
There is no guarantee ahead of time regarding how many times the loop will iterate

Syntax:
while condition:
    statements
'''

test_num=int(input("Enter the positive integer as number of prints you desire: "))
i=0
while i<test_num:
    print("Hello! This is Edureka-{}".format(i))
    i+=1