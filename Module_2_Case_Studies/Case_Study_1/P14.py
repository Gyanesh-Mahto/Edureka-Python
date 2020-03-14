'''
14. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0). 
Example: If the following n is given as input to the program: 5 Then, the output of the program should be: 3.55
'''
n=int(input("Please enter a number: "))
i=1
k=0
sum=0
while i<=n:
    k=i+1           #k will be always 1 more than i
    sum+=(i/k)      #it will do sum of divisions
    i+=1            #i is incremented
print("{:0.2f}".format(sum))    #{:0.2f} will round off decimal point to 2 digits only. like 3.55000000 to 3.55

#I/P: 5
#O/P: 3.55