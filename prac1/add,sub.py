def add(x,y):
    add=x+y
    print(add)

def mul(x,y):
    mul=x*y
    print(mul)

def sub(x,y):
    sub=x-y
    print(sub)

def dev(x,y):
    dev=x/y
    print(dev)

while(1):
    print('1.ADD')
    print('2.SUB')
    print('3.MUL')
    print('4.DEV')
    print('5.EXIT')
    i=int(input('ENTER YOUR CHOICE: '))
    if(i>=1 and i<=4):
        x=int(input('Eter first int value: '))
        y=int(input('Enter second int value: '))
    if(i==1):
        add(x,y)
    elif(i==2):
        sub(x,y)
    elif(i==3):
        mul(x,y)
    elif(i==4):
        dev(x,y)
    elif(i==5):
        print('OPERATION EXIT')
        break
    else:
        print('WRONGT INPUT')



