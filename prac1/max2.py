print('Enter three number:')
x=int(input())
y=int(input())
z=int(input())

if(x>y and x>z):
    max=x
elif(y>z and y>x):
    max=y
else:
    max=z

print('max number is:',z)