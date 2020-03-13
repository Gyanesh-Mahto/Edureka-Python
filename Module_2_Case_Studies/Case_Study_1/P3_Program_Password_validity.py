'''
3.A website requires a user to input username and password to register.
Write a program to check the validity of password given by user.
Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Hint: In case of input data being supplied to the question, it should be assumed to be a 
console input
'''
user_name="Gyan"
set_password="Gya@48nesh"
username=input("Please enter user_name: ")
if user_name==username:
    password=input("Please enter password: ")
    passw_list=list(password.strip())
    #print(passw_list[i])
    length=len(passw_list)
    #print(length)
    i=0
    cap_letter=0
    small_letter=0
    num=0
    char=0
    count=0
    for i in range(length):
        if length>=6 and length<=12:
            count+=1
        if passw_list[i]>='a' and passw_list[i]<='z':
            small_letter+=1
        if passw_list[i]>='A' and passw_list[i]<='Z':
            cap_letter+=1
        if passw_list[i]>='0' and passw_list[i]<='9':
            num+=1
        if passw_list[i]=='@' or passw_list[i]=='$' or passw_list[i]=='#':
            char+=1

    if count<length:
        print("Please enter Password of minimum length of 6 digit and maximum length of 12 digit")        
    elif small_letter<1:
        print("Please enter atleast 1 small letter between a-z")
    elif cap_letter<1:
        print("Please enter atleast 1 Capital letter between A-Z")
    elif num<1:
        print("Please enter atleast 1 number between 0-9")
    elif char<1:
        print("Please enter atleast 1 special character from $,#,@")
    else:
        print("Welcome!!! Valid and Correct Password")
else:
    print("Incorrect Username, Please enter correct Username")