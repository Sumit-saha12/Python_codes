emps={}

m=int(input('enter number of records:'))
n=int(input('enter number of field:'))

key=['id','name','salary']

for j in range(m):
    print('enter the records of employee:',j+1)
    emp={}
    for i in range(n):
        if(i==0):
           print('enter the',key[i],':',end=" ")
           value=input()
        if(i==1):
            print('enter the',key[i],':',end=" ")
            value=input()
        if(i==2):
            print('enter the',key[i],':',end=" ")
            value=input()

        emp[key[i]]=value
    r="emp"+str(j+1)
    emps[r]=emp

print('ID\tNAME\tSALARY')
for emp in emps.values():
    for x in emp.values():
        print(x,end='\t')
    print()