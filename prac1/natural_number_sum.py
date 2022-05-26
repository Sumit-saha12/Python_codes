
n=int(input('Enter the natural number: '))

i=1
s=0

print('Natural numbers are:')

while(i<=n):
    print(i,end=" ")
    s=s+i
    i=i+1
print('\nSum of',n,'natural number is:',s)

