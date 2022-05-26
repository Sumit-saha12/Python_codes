a=[]
n=int(input('ENTER THE NUMBER OF DATA:'))
for i in range(n):
    x=int(input('ENTER THE DATA:'))
    a.append(x)

for x in a:
    print(x,end=" ")

key=int(input('\nENTER THE DATA WHICH YOU WANT SEARCH: '))
f=0
for x in a:
    if(x==key):
        f=1
        break
if(f==1):
    print('THE DATA',key,'IS AVAILABLE AT',a.index(key),'th POSITION')
else:
    print('DATA IS NOT FOUND')