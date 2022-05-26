print('Enter three number:')
x=int(input())
y=int(input())
z=int(input())

if(x>z):
    if(x>y):
        max=x;
    else:
        max=y
else:
    if(z>y):
        max=z
    else:
        max=y

print('max value is',max)