n=int(input('enter number: '))
for i in range(n):
    for j in range(n+1):
        if (i==j):
            continue
        print(i," ",j)