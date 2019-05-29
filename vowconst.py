ch=input("enter the letter")
a=['a','e','i','o','u','A','E','I','O','U']
if((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
    if (ch in a):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
    
