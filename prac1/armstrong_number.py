n=int(input('Enter the number: '))

s=0
c=0
t=n
k=n

while(t!=0):
    t=int(t/10)
    c=c+1

while(n!=0):
    a=n%10
    n=int(n/10)
    s=s+(pow(a,c))

if(k==s):
    print(k,'is a armstrong number')
else:
    print(k,'is not a armstrong number')