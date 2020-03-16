#File one.py
def fun():
    print("fun() in one.py")

print("top level in one.py")

if __name__=="__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported in other module")

'''
O/P:
top level in one.py
one.py is being run directly
'''
'''
Explanation: Here fun() is decalred but not called. So, "top level in one.py is printed" and as
nothing is imported, so, __name__ attribute has same name as of __main__which is "P2_one".
So, "one.py is being run directly is printed".
'''