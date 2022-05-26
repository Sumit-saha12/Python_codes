
def equation(x):
    a = (x * x * x) - (9 * x) + 1
    return a
##m=int(input('ENTER LOWER LIMIT:'))
##n=int(input('ENTER UPPER LIMIT:'))
l = 1
xn = 0
xn1 = 0
delta = 1
a=-1.0
b=-1.0

for i in range(0,a==-1.0 or b==-1.0,+1):
    print(a, b)
    k = equation(i)
    print(k)
    if k< 0.00:
        a = i
    elif k>0.00:
        b=i



print('steps    f(a)<0    f(b)>0    xn1=(a+b)/2    f(xn1)\n')
while delta >= 0.01:
    xn = xn1
    xn1 = (a + b) / 2
    k = equation(xn1)
    print(l, a, b, xn1, k)
    if k < 0:
        a = xn1
    elif k > 0:
        b = xn1
    delta = abs(xn1 - xn)
    l = l + 1

print('the root is xn1=', xn1)
