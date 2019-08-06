c=int(input())
a=list(str(input()))
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in vowel:
        a.remove(i)
print("".join(a)[::-1])
