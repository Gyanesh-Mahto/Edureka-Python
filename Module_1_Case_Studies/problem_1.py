'''
1.Write a program which will find factors of given number and find whether the factor is even or odd.Hint: Use Loop with if-else statements
'''

n=int(input("Please enter any number: "))
i=1
while i<=n:
    if(n%i==0):
        if(i%2==0):
            print(i,"Even")
        else:
            print(i,"Odd")
    i+=1