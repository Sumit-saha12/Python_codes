#1st process

"""n=int(input('ENTER THE NUMBER OF ROW:'))
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if(a==1):
            print(1,end=" ")
            a=a+1
        else:
            print(0,end=" ")
            a=a-1

    print()"""

#2nd process

n=int(input('ENTER THE NUMBER OF ROW:'))
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a%2,end=" ")
        a=a+1

    print()