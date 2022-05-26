"""a=[4,5,6,1,2,3,2,1,10,546,8,6]
#print(a)
for i in a:
    print(i,end=" ")
a=[]
n=int(input('ENTER THE NUMBER OF DATA:'))
for i in range(n):
    x=int(input('ENTER THE DATA:'))
    a.append(x)

for x in a:
    print(x,end=" ")

x=[1,5,6,9,4,6,5,5,1,2,36,45,5,4,5,66]
print(len(x))
print(x[1])
print(x[-1])
x[1]=22
print(x)

print(x[2:5])
print(x[3:])
print(x[:6])
print(x[-4:-1])

x.append('hipo')
print(x)

x.insert(4,'ssssss')
print(x)

x.pop()
print(x)

x.pop(2)
print(x)

x.remove(5)
print(x)

print(x[::-1])

x.reverse()
print(x)
print(x[::-1])

print(x.count(5))

a=[1,2,3]
b=['sumit','rahul']
c=a+b
print(c)"""


a=[]
n=int(input('ENTER THE NUMBER OF DATA:'))
for i in range(n):
    x=int(input('ENTER THE DATA:'))
    a.append(x)

for x in a:
    print(x,end=" ")

a.sort()
print('\n',a)