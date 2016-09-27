import sys
class Student(object):
    name = ''
    id = ''
    add = ''
    sex = ''
    math = 0
    physics = 0
    chemistry = 0
    def __init__(self, name, id, add, sex, math, physics, chemistry):
        self.name = name
        self.id = id
        self.add = add
        self.sex = sex
        self.math = float(math)
        self.physics = float(physics)
        self.chemistry = float(chemistry)

    def displayStudent(self):
        Students = StudentTmp.read_from_file()
        f = open("input.txt", "r")
        n = int(f.readline())
        print 'Total Student: ', n
        print Students

    def enterInforStudent(self):
        Students = StudentTmp.read_from_file()
        Stu = []
        for Student in Students:
            s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
            Stu.append(s)
        f = open("input2.txt", "r") #mo file de doc va ghi de lai t
        k = int(f.readline())
        fo = open("input2.txt", "w+")
        n = int(raw_input('Nhap n: '))
        for i in range(n):
            print 'Nhap thong tin cho Student ',i+1
            id = str(k+i+1)
            name = raw_input('Nhap Name: ')
            add = raw_input('Nhap add: ')
            sex = raw_input('Nhap Sex: ')
            math = float(raw_input('Nhap diem Toan: '))
            physics = float(raw_input('Nhap diem ly: '))
            chemistry = float(raw_input('Nhap diem hoa: '))
            i+=1
            Str = id +' '+name+' '+add+' '+sex+' '+str(math)+' '+str(physics)+' '+str(chemistry)
            print Str
            Stu.append(Str)

        k = k+n
        a = str(Stu)
        a = a.lstrip('[')  # Xoa bo dau [] , ''
        a = a.rstrip(']')
        a = a.replace(",", "\n", k - 1)
        a = a.replace("'", "", k * 2)
        #print str(k)+'\n'+a
        fo.write(str(k)+'\n'+a)
        f.close()
        fo.close()

    def sorted(self):
        Students = StudentTmp.read_from_file()
        f = open("input2.txt", "r")
        n = int(f.readline())
        StrA = []
        fo = open("input2.txt", "w+")
        for Student in Students:
            s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
            StrA.append(s)
        StrA.sort()  # lay all list SV ra va sap xep theo sort() - ID
        #print StrA
        a = str(StrA)
        a = a.lstrip('[')  # Xoa bo dau [] , ''
        a = a.rstrip(']')
        a = a.replace(",", "\n", n - 1)
        a = a.replace("'", "", n * 2)
        fo.write(str(n)+'\n'+a)
        fo.close()

    def read_from_file(self):
        Students = []
        f = open("input2.txt", "r")
        n = int(f.readline())
        #print 'Total Student: ', n
        i = 1
        for i in range(n):
            line1 = f.readline()
            line1.strip()
            id, name, add, sex, math, physics, chemistry = line1.split()
            Student ={"id": id, "name": name, "add": add, "sex": sex, "math": math, "physics": physics,
                       "chemistry": chemistry} #dict
            Students.append(Student)
        return Students

    def deleteStudent(self):
        StudentsA = StudentTmp.read_from_file()
        Students = StudentsA #list
        #fo = open('input.txt', 'a+')
        fi = open('input2.txt', 'w+')
        key = raw_input('Nhap id Student can xoa: ')
        for Student in Students:
            if (Student['id'] == key):
                Str = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                    Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                print Str
                Students.remove(Student)
                print Students

        writeStr = []
        k = 0
        for Student in Students: #Students sau khi remove
            Str = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                    Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
            k = k+1
            writeStr.append(Str)
            a = str(writeStr)
        a = a.lstrip('[')  #Xoa bo dau [] , ''
        a = a.rstrip(']')
        a = a.replace("," , "\n", k-1)
        a = a.replace("'" , "", k*2)
        print a
        fi.write(str(k)+'\n'+a)
        print 'Deleted!'

    def editStudent(self):
        Students = StudentTmp.read_from_file()

        flag = 1
        while True:
            while flag == 1:
                try:
                    key = raw_input('Nhap id Student can sua: (01 ->28)')
                    for Student in Students:
                        if (Student['id'] == key):
                            flag = 0
                            Str = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                                Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                            name = Student['name']
                            id = Student['id']
                            add = Student['add']
                            sex = Student['sex']
                            print 'ID =',key,': ', Str
                            Students.remove(Student)  # xoa Student roi luu lai
                            #edit_menu()
                except ValueError, e:
                    print 'ID Not Exists!', e.message


            writeStr = []
            k = 1
            for Student in Students:  # Students sau khi remove
                St = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                k = k + 1
                writeStr.append(St)

            def edit_Name():
                tname = raw_input('Enter Name New: ')
                Str_new = Str.replace(name, tname)
                print Str_new
                writeStr.append(Str_new)
                #Students.remove(Student)  # xoa Student roi luu lai
                saved()

            def editAdd():
                tAdd = raw_input('Enter Add New: ')
                Str_new = Str.replace(add,tAdd)
                print Str_new
                writeStr.append(Str_new)
                saved()

            def editSex():
                tSex = raw_input('Enter Sex New: ')
                Str_new = Str.replace(sex,tSex)
                print Str_new
                writeStr.append(Str_new)
                saved()
            def saved():
                fi = open('input2.txt', 'w+')
                a = str(writeStr)
                a = a.lstrip('[')  # Xoa bo dau [] , ''
                a = a.rstrip(']')
                a = a.replace(",", "\n", k - 1)
                a = a.replace("'", "", k * 2)
                #print a
                fi.write(str(k) + '\n' + a)
                print 'Edited!'
                fi.close()

            #def edit_menu():
            print "Select: Edit Student"
            print "1. Edit name: "
            print "2. Edit SBD: "
            print "3. Edit Add:"
            print "4. Edit Sex:"
            print "0. Return"

            while True:
                try:
                    choice = (raw_input("Nhap lua chon 0 -> 4: "))
                    choice = int(choice)
                    if choice == 0:
                        print 'Return...'
                        StudentTmp.menu()
                        break
                    elif choice == 1:
                        print "1. Edit name: "
                        edit_Name()
                        break
                    elif choice == 2:
                        print "2. Edit SBD "
                        #editId()
                        print 'Sorry, Id khong sua dc :) '
                        break
                    elif choice == 4:
                        print "4. Edit Sex"
                        editSex()
                        break
                    elif choice == 3:
                        print "3. Edit Add"
                        editAdd()
                        break
                    else:
                        print("Choose not exists!! ")
                except ValueError:
                    print 'Nhap sai!!'
    def search(self):
        Students = StudentTmp.read_from_file()
        fo = open('timkiem2.txt', 'a')  #mo file va ghi them vao cuoi file

        def tim_kiem_diem():
            k = 0
            aa = '\n\tResult tim kiem diem:\n'
            fo.write(aa)
            tScore = float(raw_input('Nhap diem can tim: '))

            for Student in Students:
                if (float(Student['math']) == tScore or float(Student['physics']) == tScore or float(Student['chemistry']) == tScore):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    #print s
                    writeStr = []
                    writeStr.append(s)
                    a = str(writeStr)
                    a = a.lstrip('[')  # Xoa bo dau [] , ''
                    a = a.rstrip(']')
                    a = a.replace(",", "\n", k - 1)
                    a = a.replace("'", "", k * 2)
                    print a
                    fo.write(a+'\n')
                    #print 'saved!'

        def tim_kiem_name():
            k  =0
            aa = '\n\tResult tim kiem name:\n'
            fo.write(aa)
            tName = raw_input('Nhap name can tim: ')

            for Student in Students:
                if (Student['name'] == tName):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    # print s
                    writeStr = []
                    writeStr.append(s)
                    a = str(writeStr)
                    a = a.lstrip('[')  # Xoa bo dau [] , ''
                    a = a.rstrip(']')
                    a = a.replace(",", "\n", k - 1)
                    a = a.replace("'", "", k * 2)
                    print a
                    fo.write(a+'\n')

        def tim_kiem_id():
            k = 0
            aa = '\n\tResult tim kiem id:\n'
            fo.write(aa)
            tId = (raw_input('Nhap SBD can tim: '))

            for Student in Students:
                if (Student['id'] == tId):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    # print s
                    writeStr = []
                    writeStr.append(s)
                    a = str(writeStr)
                    a = a.lstrip('[')  # Xoa bo dau [] , ''
                    a = a.rstrip(']')
                    a = a.replace(",", "\n", k - 1)
                    a = a.replace("'", "", k * 2)
                    print a
                    fo.write(a+'\n')

        def tim_kiem_tong_diem():
            k = 0
            aa = '\n\tResult tim kiem tong diem:\n'
            fo.write(aa)
            tScore = float(raw_input('Nhap tong diem can tim: '))
            Students = StudentTmp.read_from_file()
            for Student in Students:

                if ((float(Student['math']) + float(Student['physics']) + float(Student['chemistry'])) == tScore):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    # print s
                    writeStr = []
                    writeStr.append(s)
                    a = str(writeStr)
                    a = a.lstrip('[')  # Xoa bo dau [] , ''
                    a = a.rstrip(']')
                    a = a.replace(",", "\n", k - 1)
                    a = a.replace("'", "", k * 2)
                    print a
                    fo.write(a+'\n')


        print "Search Student:"
        print "1. tim kiem theo tong so diem: "
        print "2. tim kiem theo SBD: "
        print "3. tim kiem theo Name"
        print "4. tim kiem theo diem"
        print "0. Return"

        while True:
            try:
                choice = (raw_input("Nhap lua chon 0 -> 4: "))
                choice = int(choice)
                if choice == 0:
                    print 'Return...'
                    #StudentTmp.menu()
                    fo.close()
                    break
                elif choice == 1:
                    print "1. tim kiem theo tong so diem: "
                    StudentTmp.sorted()
                    tim_kiem_tong_diem()
                elif choice == 2:
                    print "2. tim kiem theo SBD: "
                    StudentTmp.sorted()
                    tim_kiem_id()
                elif choice == 3:
                    print "3. tim kiem theo Name"
                    StudentTmp.sorted()
                    tim_kiem_name()
                elif choice == 4:
                    print "4. tim kiem theo diem"
                    StudentTmp.sorted()
                    tim_kiem_diem()
                else:
                    print("khong co lua chon nay ")
            except ValueError:
                print 'Nhap sai!!'

    def menu(self):
        print "Student manager"
        print "1. Read & View list Student from file"
        print "2. input information Student form keyboard"
        print "3. Edit a Student"
        print "4. Delete a Student"
        print "5. Search"
        print "6. Statistics"
        print "0. Exit"
        while True:
            try:
                choice = raw_input("\nMain - Choose 0 -> 5: ")
                choice = int(choice)
                if choice == 0:
                    print 'Exiting...'
                    sys.exit(1)
                elif choice == 1:
                    print 'List Student:'
                    StudentTmp.displayStudent()
                elif choice == 2:
                    print '2. input information Student form keyboard'
                    StudentTmp.enterInforStudent()
                elif choice == 3:
                    print '3. Editing'
                    StudentTmp.editStudent()
                elif choice == 4:
                    print '4. Delete'
                    StudentTmp.deleteStudent()
                elif choice == 5:
                    StudentTmp.search()
                else:
                    print("Choose not exists")
            except ValueError:
                print 'Nhap sai!!'


if __name__ == '__main__':
    StudentTmp = Student('id','name', 'add', 'sex', 0,0,0)
    StudentTmp.sorted()
    StudentTmp.menu()
