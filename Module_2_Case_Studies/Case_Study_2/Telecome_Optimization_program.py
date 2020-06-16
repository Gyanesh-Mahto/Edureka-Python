'''
Case Study II 
 
Domain – Telecom 
focus – Optimization 
 
Business challenge/requirement:
LifeTel  Telecom is the latest entrant in the highly competitive Telecom market of Singapore.  It issues SIM to the verified users.  
Till now verification was manual through the photocopy of approved id card document. However government has recently introduced 
Social ID called Reference ID which is mapped to fingerprint of user. LifeTel should now verify user against the fingerprint and Reference ID 
 
Key issues:
Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID and finger print 

Considerations:
System should be secure 
 
Data volume - NA 
 
Additional information - NA 
 
Business benefits:
Company will be able to quickly issue SIM to user and expected gain in volume is approximately 10 times as the manual process of 
verification is replaced with secure automated system 
 
Approach to Solve You have to use fundamentals of Python taught in module 2:
1. Read the input from command line – Reference ID 
2. Check for validity – it should be 12 digits and allows on number and alphabet       
3. Encrypt the Reference ID and print it for reference 

Enhancements for code:
You can try these enhancements in code 
1. Allow some special characters in Reference ID 
2. Give the option for decryption to user  
''' 
import cryptography
import sys

reference_id=input("Please enter your reference ID: ")      #1. Read the input from command line – Reference ID
list_ref=list(reference_id.strip())
l=len(list_ref)
if l==12:
    #print(list_ref)
    #l=len(list_ref)
    #print(l)
    alpha_letters=0
    num=0
    special_char=0
    for i in range(l):          #2. Check for validity – it should be 12 digits and allows on number and alphabet 
        if list_ref[i]>='a' and list_ref[i]<='z':
            alpha_letters+=1
        if list_ref[i]>='A' and list_ref[i]<='Z':
            alpha_letters+=1
        if list_ref[i]>='0' and list_ref[i]<='9':
            num+=1
        if list_ref[i]=='@' or list_ref=='#' or list_ref=='$':      #1. Allow some special characters in Reference ID 
            special_char+=1
    if alpha_letters>=1 and num>=1 and special_char>=1:
        from cryptography.fernet import Fernet      #3. Encrypt the Reference ID and print it for reference
        key=Fernet.generate_key()
        #print(key)
        file=open("Key.key", 'wb')
        file.write(key)
        file.close()
        encoded=reference_id.encode()       #encoding the data
        f=Fernet(key)
        encrypted=f.encrypt(encoded)
        print("Reference Id is encrypted as follows:")
        print(encrypted)        #Printing encrypted data for reference
    else:
        print("Please use combination of number, alphabets and special characters")
        sys.exit()
    user_input=input("Do you want to decrypt data: ")     #2. Give the option for decryption to user
    if user_input=='Y' or user_input=='y':
        file=open("Key.Key", 'rb')
        key=file.read()
        file.close()
        print(key)
        f2=Fernet(key)
        decrypted=decrypted=f2.decrypt(encrypted)
        print(decrypted)
        original_reference_id=decrypted.decode()
        print(original_reference_id)
    else:
        print("Thanks, Your data is safe!!!")
else:
    print("Your Reference ID should be 12 digit. Please enter 12 digit Reference ID")

'''
I/P:
----
Please enter your reference ID: qwert12345@#
O/P:
----
Reference Id is encrypted as follows:
b'gAAAAABea1MHZ5qIuQydO6IyAfLWXCaEHA2QrBTPiCZnIFUHstzJmYntNIxqoOA5-UNEpXqPKW8TsLyMZoao7aRKoF-JXHGFvQ=='
Do you want to decrypt data: Y
b'gbJG3qGxfg7-bxtefwiDffqsUF6YOPXjpI64FUG0z3c='
b'qwert12345@#'
qwert12345@#
'''
