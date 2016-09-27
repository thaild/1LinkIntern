class Student(object):
    """
    Returns a ```Student``` object with the given name, branch and year.

    """
    name = ''
    age = 0
    def __init__(self, name, age):
            self.name = name
            self.age = age


    def load_file(self):
        Students = []
        f = open("input.txt", "r")
        n = int(f.readline())
        print 'Total Student: n', n
        for i in range(n):
            line1 = f.readline()
            name, age = line1.split()
            Student = {"name": name, "age": age}
            Students.append(Student)
        return Students
    def print_details(self):
        """
        Prints the details of the student.
        """
        print("Name:", self.name)
        print("Age:", self.age)


    def danh_sach(self):
        for i in Student:
            print("Name:", self.name)
            print("Age:", self.age)

    def tim_kiem(self):
        key = raw_input("tim theo ten: ")
        if key in Student:
            print ("Tim thay : %s : %s" % (key, Student[key]))
        else:
            print ("Tim ko thay %s" %(key))

if __name__ == '__main__':
    temp = Student()
    temp.load_file()