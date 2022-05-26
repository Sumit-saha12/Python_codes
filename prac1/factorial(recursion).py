def function(n):
    if n==1 or n==0:
        return 1
    else:
        f=n*function(n-1)
        return f

n=int(input('ENTER NUMBER WHICH YOU WANT FACTORIAL: '))
print(function(n))