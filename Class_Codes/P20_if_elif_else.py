'''
Syntax:
if my_condition:
    (Indentation) statement
elif my_condition:
    (Indentation) statement
else:
    (Indentation) statement
'''
'''
if-else conditions
'''
name='Gyanesh'

name_list=['Anubhav', 'Yuyutsu', 'Abhijeet', 'Ranvijay', 'Gyanesh', 'Manoj']

if name in name_list:
    print(name)
    print(True)
else:
    print(name)
    print(False)

#O/P:
#Gyanesh
#True
'''
Here in operator checks whether sequence of input is prsent in a list or not.
'''

name='Vivek'

if name in name_list:
    print(name)
    print(True)
else:
    print(False)

#O/P:
#Vivek
#False
'''
Here output is False because name 'Vivek' is not present in name_list.
'''

'''
if-elif-else conditions:
'''
m_name_list=['Anubhav', 'Yuyutsu', 'Abhijeet', 'Ranvijay', 'Gyanesh', 'Manoj']
f_name_list=['Vimmi', 'Ruchi', 'Kusum', 'Pooja', 'Hithaishi', 'Riya']

name='Gyanesh'

if name in m_name_list:
    print("Name is a member of m_name_list")
elif name in f_name_list:
    print("Name is a member of f_name_list")
else:
    print("Name is not present in both lists")

#O/P:
#Name is a member of m_name_list

m_name_list=['Anubhav', 'Yuyutsu', 'Abhijeet', 'Ranvijay', 'Gyanesh', 'Manoj']
f_name_list=['Vimmi', 'Ruchi', 'Kusum', 'Pooja', 'Hithaishi', 'Riya']

name='Riya'

if name in m_name_list:
    print("Name is a member of m_name_list")
elif name in f_name_list:
    print("Name is a member of f_name_list")
else:
    print("Name is not present in both lists")

#O/P:
#Name is a member of f_name_list

m_name_list=['Anubhav', 'Yuyutsu', 'Abhijeet', 'Ranvijay', 'Gyanesh', 'Manoj']
f_name_list=['Vimmi', 'Ruchi', 'Kusum', 'Pooja', 'Hithaishi', 'Riya']

name='John'

if name in m_name_list:
    print("Name is a member of m_name_list")
elif name in f_name_list:
    print("Name is a member of f_name_list")
else:
    print("Name is not present in both lists")

#O/P:
#Name is not present in both lists

'''
Q. What if name is present in both lists
Solution: In which ever condtion name is found, from there it exits the program after printing that statement
'''

m_name_list=['Anubhav', 'Yuyutsu', 'Abhijeet', 'Ranvijay', 'Gyanesh', 'Manoj', 'Pintu']
f_name_list=['Vimmi', 'Ruchi', 'Kusum', 'Pooja', 'Hithaishi', 'Riya', 'Pintu']

name='Pintu'

if name in m_name_list:
    print("Name is a member of m_name_list")
elif name in f_name_list:
    print("Name is a member of f_name_list")
else:
    print("Name is not present in both lists")

#O/P:
#Name is a member of m_name_list