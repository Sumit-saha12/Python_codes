class employee:

    def get(self):
        self.eid = input('enter eid:')
        self.ename = input('enter ename:')
        self.salary = int(input('enter salary:'))

    def display(self):
        print(self.eid, ':', self.ename, ':', self.salary)


"""ob=employee()
ob.get()
ob.display()

ob1=employee()
ob1.get()
ob1.display()

ob2=employee()
ob2.get()
ob2.display()

ob1.display()"""

n=int(input('enter the no. of epmloyee:'))

#array_of_object
emp=[]
for i in range(1,n+1):
    print('enter the record for employee no:',i)
    ob=employee()
    ob.get()
    emp.append(ob)

for i in range(n):
    emp[i].display()
