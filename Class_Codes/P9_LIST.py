'''
Lists: List is an ordered set of elements enclosed within square brackets. The main differences between Lists and Tuples are:
->Lists are enclosed in brackets[] and Tuples are enclosed within paranthesis()
->Lists are Mutable and Tuples are immutable
->Tuples are faster than Lists.
'''

List1=[1,2,3,4,5,'6', 7j+8, 'a']
print(List1)
print(id(List1))

#O/P:
#[1, 2, 3, 4, 5, '6', (8+7j), 'a']
#30225912

List1[0]=100
print(List1)
print(id(List1))

#O/P:
#[100, 2, 3, 4, 5, '6', (8+7j), 'a']
#30225912

'''
Here list gets modified when we change particular element, but the address is same for both time. This is the nature of mutable data types.

'''