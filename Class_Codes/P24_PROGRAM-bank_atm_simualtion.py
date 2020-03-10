'''
WAP in python that effectively simulates a bank ATM:

Enter 4 digit pin------>Check balance
                    |
                    |-->Make a withdrawal
                    |
                    |-->Pay in
                    |
                    |-->Return Card
'''
password='4321'
balance=1000
withdrawal_amount=0
pay_in_amount=0

password_1=input("Please enter your 4 digit pin: ")

if password_1==password:
    print("Please enter your choice: ")
    print("1. Check Balance")
    print("2. Make a withdrawal")
    print("3. Pay in")
    print("4. Return Card")
    selection=int(input("Please enter here: "))

    if selection==1:
        print("Balance={}".format(balance))
    elif selection==2:
        withdrawal_amount=int(input("Please enter withdrawal amount: "))
        if withdrawal_amount>balance:
            print("Insufficient funds")
        else:
            balance=balance-withdrawal_amount
            print("Congrats!!! Withdrawal Successful")
            print("Current Balance after Withdrawal={}".format(balance))
    elif selection==3:
        pay_in_amount=int(input("Please enter pay in amount: "))
        balance=balance+pay_in_amount
        print("Congrats!!! Pay In Successful")
        print("Current Balance after Pay in={}".format(balance))
    elif selection==4:
        print("Returning your card")
    else:
        print("Incorrect input")
else:
    print("Incorrect Password")



