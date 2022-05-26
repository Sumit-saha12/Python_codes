n=int(input('Enter the number: '))

s=0
k=n

while(n!=0):
    a=n%10
    n=int(n/10)
    s=(s*10)+a

if(k==s):
    print(k,'is a palindrom number')
else:
    print(k,'is not a palindrom number')