'''
3.Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number.
The numbers obtained should be printed in a comma separated sequence on a single line.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
Divide each digit with 2 and verify is it even or not.
'''

i=1000
i_3=0
for i in range(1000,3001):
    i_1=str(i)
    i_2=list(i_1.strip())
    #print(i_2)
    l=len(i_2)
    #print(l)
    j=0
    k=0
    for j in range(l):
        i_3=int(i_2[j])
        #print(i_3)
        if i_3%2!=0:
            break
            #continue
        else:
            j+=1
        if j==l:
            i_4=list(i_2)
            new=""
            for x in i_4:
                new=new+x
            print(new,",")
        else:
            pass
        