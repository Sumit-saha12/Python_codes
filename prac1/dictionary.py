"""student={
    "name":"sumit",
    "roll no": 1,
    "age": 20,
}

print(student)
print(student['name'])
print(student['age'])
for s in student:
    print(s)
print()
student['age']=22
for s in student.values():
    print(s)
print()

for s in student:
    print(s,'\t:',student[s])"""

myfamily={
    "child1" : {
    "name" : "sumit",
    "age" : 22
    },
    "child2" : {
    "name" : "souvik",
    "age" : 12
    }

}

print(myfamily)
print()
print('NAME\tAGE')
for s in myfamily.values():
    for x in s.values():
        print(x,end='\t')
    print()
