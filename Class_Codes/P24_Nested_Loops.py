'''
Nested Loops: Nested Loop basically means a loop inside a loop. It can be a for loop inside a while loop and vice-versa. It can also be a While loop
inside a while loop or for loop inside a for loop.
'''

count=1
for i in range(10):
    print(str(i)*i)

    for j in range(0, i):
        count+=1
'''
O/P:
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''