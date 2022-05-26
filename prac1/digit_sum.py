n=int(input('Enter digit: '))

s=0

while(n!=0):
    a=n%10
    n=int(n/10)
    s=s+a

print('Sum of digit is',s)
