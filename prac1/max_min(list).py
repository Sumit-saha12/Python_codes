a=[]
n=int(input('ENTER THE NUMBER OF DATA:'))
for i in range(n):
    x=int(input('ENTER THE DATA:'))
    a.append(x)

for x in a:
    print(x,end=" ")

max=a[0]
min=a[0]

for x in a:
    if(x>max):
        max=x

for x in a:
    if(x<min):
        min=x

print('\nmaximum element is:',max)
print('\nminimum element is:',min)