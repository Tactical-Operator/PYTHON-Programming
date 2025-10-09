# accessing in reverse order using the concept of negative indexing i.e -1=length of the string(n) 
# and -(length of string+1)=the first position
str='Ashwin Jadhav'
n=len(str)
print(str)
print()
i=-1
while i>=-n:
    print(str[i],end=' ')
    i-=1