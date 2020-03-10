'''
Loop Control Statements: Loop Control Statements change execution from its normal sequence. When execution leaves a scope, all automatic objects
that were created in that scope are destroyed.

Control Statement ------------------------------------------------->Description
break statement---------------------------> Terminates the loop statement and transfers execution to the statement immediately following the loop.
continue statement------------------------> Causes the loop to skip the remainder of its body and immediately retest prior to reiterating.
pass statement----------------------------> The pass statement in python is used when a statement is required syntactically but you do not want any 
command or code to execute.
'''

for i in range(10):
    print(i)
    if i==5:
        break
print("========================================")
'''
O/P:
0
1
2
3
4
5   <----------for loop is terminated due to break
'''
for i in range(10):
    if i==5:
        continue
    print(i)
print("========================================")
'''
O/P:
0
1
2
3
4
6       <----5 is skipped due to continue
7
8
9
'''
for i in range(10):
    print(i)
    if i==5:
        pass
print("========================================")
'''
O/P:
0
1
2
3
4
5   <---No effect due to pass
6
7
8
9
'''