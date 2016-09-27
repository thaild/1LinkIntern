from solution import *

Students = []
f = open("input.txt", "r")
n = int(f.readline())
print n
for i in range(n):
    line1 = f.readline()
    name, id, add, sex, math, physics, chemistry = line1.split()
    Student = {"name": name, "id": id, "add": add, "sex": sex, "math": math, "physics": physics,
               "chemistry": chemistry}
    Students.append(Student)
    print Student