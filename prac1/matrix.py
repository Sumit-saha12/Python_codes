r = int(input('Enter the number of row:'))
c = int(input('Enter the number of column:'))

matrix = []

for i in range(r):
    a = []
    for j in range(c):
        print('Enter the data in row',i,'col',j,':')
        x = int(input())
        a.append(x)
    matrix.append(a)

for x in matrix:
    for y in x:
        print(y, end=' ')
    print()
