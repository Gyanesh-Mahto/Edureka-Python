'''
2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''
str_1=input("Please enter a string:")
word=str_1.strip()
word_1=list(word)
print(word_1)
word_1.sort()
print(word_1)