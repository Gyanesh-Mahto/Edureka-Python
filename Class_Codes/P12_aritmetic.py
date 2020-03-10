#Arithmetic Operators:
'''
---------------
Addition:       a+b
Subtraction:    a-b
Multiplication: a*b
Division:       a/b
Modulus:        a%b
Exponent:       a**b
Floor Division: a//b
'''
var_1=100
var_2=202.5

str_1='A'
str_2="Edureka"

print(var_1+var_2)
print(str_1+str_2)
#O/P:
#302.5
#AEdureka

print(var_1-var_2)      #-102.5
#print(str_1-str_2)     #TypeError: unsupported operand type(s) for -: 'str' and 'str'


print(var_1*var_2)      #20250.0
#print(str_1*str_2)     #TypeError: can't multiply sequence by non-int of type 'str'
print(str_1*5)          #AAAAA
#So, if any string is multiplied with numberic value(integer only) then that string will be multiplied that much times of number.
#print(str_1*5.5)        #TypeError: can't multiply sequence by non-int of type 'float'

print(var_1/var_2)      #0.49382716049382713
#print(str_1/str_2)      #TypeError: unsupported operand type(s) for /: 'str' and 'str'
#print(str_1/5)          #TypeError: unsupported operand type(s) for /: 'str' and 'int'

#Modulous(%)<---It gives remainder
print(20%5)         #0
print(5%20)         #5

#Exponenet
print(2**5)     #32

#Floor Division: a//b<-----It removes decimal values from the end result.
print(5//3)     #1