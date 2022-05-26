a=[]
n=int(input('ENTER THE NUMBER OF DATA:'))
for i in range(n):
    x=int(input('ENTER THE DATA:'))
    a.append(x)

for x in a:
    print(x,end=" ")

for i in range(0,(n-1)):
    for j in range(0,(n-i-1)):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]

print('\nAFTER SORTING')
for x in a:
    print(x,end=" ")
