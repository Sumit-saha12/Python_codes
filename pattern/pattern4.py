n=int(input('ENTER THE NUMBER OF ROW:'))

for i in range(n+1,0,-1):
    for j in range(i+1,1,-1):
        print('*',end=" ")
    print()