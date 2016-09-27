import sys
class Student(object):
    name = ''
    id = ''
    add = ''
    sex = ''
    math = 0
    physics = 0
    chemistry = 0
    def __init__( self,name,id,add,sex,math,physics,chemistry ):
        self.name = name
        self.id = id
        self.add = add
        self.sex = sex
        self.math = float(math)
        self.physics = float(physics)
        self.chemistry = float(chemistry)

    def _show_student(self):
        Students = StudentTmp.read_from_file()
        print Students

    def enterInforStudent(self):
        Students = StudentTmp.read_from_file()
        Stu = []
        for Student in Students:
            s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
            Stu.append(s)
        f = open("input.txt", "r") #mo file de doc va ghi de lai t
        k = int(f.readline())
        fo = open("input.txt", "w+")
        j =1
        while j ==1 :
            try:
                n = int(raw_input('Nhap n: '))
                for i in range(n):
                    print 'Nhap thong tin cho Student ',i+1
                    id = str(k + i + 1)
                    name = raw_input('Nhap Name: ')
                    add = raw_input('Nhap add: ')
                    sex = raw_input('Nhap Sex: ')
                    math = float(raw_input('Nhap diem Toan: '))
                    physics = float(raw_input('Nhap diem ly: '))
                    chemistry = float(raw_input('Nhap diem hoa: '))
                    Str = id +' '+name+' '+add+' '+sex+' '+str(math)+' '+str(physics)+' '+str(chemistry)
                    print Str
                    Stu.append(Str)
                    j = 0

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
            except ValueError:
                print 'Nhap sai n!'

    def sorted(self):
        Students = StudentTmp.read_from_file()
        f =  open("input.txt", "r")
        n = int(f.readline())
        StrA = []
        fo = open("input.txt", "w+")
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

    def thongke(self):
        Students = StudentTmp.read_from_file()
        StrA = []

        fo = open("thongke.txt", "a+")
        def total15():
            k =0
            fo.writelines('\nStudent co total < 15:\n')
            writeStr = []
            for Student in Students:
                if ((float(Student['math']) + float(Student['physics']) + float(Student['chemistry'])) < 15):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    print s

                    writeStr.append(s)
            a = str(writeStr)
            a = a.lstrip('[')  # Xoa bo dau [] , ''
            a = a.rstrip(']')
            a = a.replace(",", "\n", k - 1)
            a = a.replace("'", "", k * 2)
            #print str(k)+'\n'+a
            fo.write(str(k)+'\n'+a)
        def total1520():
            k =0
            fo.writelines('\nStudent co total < 20:\n')
            writeStr = []
            for Student in Students:
                if (15 <= (float(Student['math']) + float(Student['physics']) + float(Student['chemistry'])) < 20):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    print s

                    writeStr.append(s)
            a = str(writeStr)
            a = a.lstrip('[')  # Xoa bo dau [] , ''
            a = a.rstrip(']')
            a = a.replace(",", "\n", k - 1)
            a = a.replace("'", "", k * 2)
            #print str(k)+'\n'+a
            fo.write(str(k)+'\n'+a)
        def total2025():
            k =0
            fo.writelines('\nStudent co total < 25:\n')
            writeStr = []
            for Student in Students:
                if (20 <= (float(Student['math']) + float(Student['physics']) + float(Student['chemistry'])) < 25):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    print s

                    writeStr.append(s)
            a = str(writeStr)
            a = a.lstrip('[')  # Xoa bo dau [] , ''
            a = a.rstrip(']')
            a = a.replace(",", "\n", k - 1)
            a = a.replace("'", "", k * 2)
            #print str(k)+'\n'+a
            fo.write(str(k)+'\n'+a)
        def total25():
            k =0
            fo.writelines('\nStudent co total >25:\n')
            writeStr = []
            for Student in Students:
                if ((float(Student['math']) + float(Student['physics']) + float(Student['chemistry'])) > 25):
                    k = k+1
                    s = Student['id'] + ' ' + Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                    print s
                    writeStr.append(s)
            a = str(writeStr)
            a = a.lstrip('[')  # Xoa bo dau [] , ''
            a = a.rstrip(']')
            a = a.replace(",", "\n", k - 1)
            a = a.replace("'", "", k * 2)
            #print str(k)+'\n'+a
            fo.write(str(k)+'\n'+a)


        print "Statistics Student:"
        print "1. total < 15: "
        print "2. 15 <= total < 20: "
        print "3. 20 <= total < 25"
        print "4. total > 25"
        print "0. Return"

        while True:
            try:
                choice = (raw_input("Nhap lua chon 0 -> 4: "))
                choice = int(choice)
                if choice == 0:
                    print 'Return...'
                    StudentTmp.menu()
                    fo.close()
                    break
                elif choice == 1:
                    print "1. total < 15 "
                    total15()
                elif choice == 2:
                    print "2. 15 <= total < 20: "
                    total1520()
                elif choice == 3:
                    print "3. 20 <= total < 25"
                    total2025()
                elif choice == 4:
                    print "4. total > 25"
                    total25()
                else:
                    print("khong co lua chon nay ")
            except ValueError:
                print 'Chon sai!!'

    def _read_file(self):
        Students = []
        f = open("input.txt", "r")
       	while f.readline() != None:
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
        fi = open('input.txt', 'w+')
        flag =1
        while flag == 1:
            try:
                key = raw_input('Nhap id Student can xoa: ')
                for Student in Students:
                    if (Student['id'] == key):
                        Str = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                            Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                        print Str
                        Students.remove(Student)

                        #print Students
                        flag = 0
            except ValueError:
                print 'Sai ID!'

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
        #print a
        fi.write(str(k)+'\n'+a)
        print 'Deleted!'

    def editStudent(self):
        Students = StudentTmp.read_from_file()
        flag = 1
        while flag == 1:
            try:
                key = int(raw_input('Nhap id Student can sua: (01 -> 26)'))
                for Student in Students:
                    if (int(Student['id']) == key):
                        flag = 0
                        Str = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                            Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                        name = Student['name']
                        id = Student['id']
                        add = Student['add']
                        sex = Student['sex']
                        print 'ID =',key,': ', Str
                        Students.remove(Student) #xoa Student roi luu lai

            except ValueError, e:
                print 'ID Not Exists! ', e.message
            writeStr = []
            k = 1
            for Student in Students:  # Students sau khi remove
                St = Student['id'] + ' ' +  Student['name'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                        Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
                k = k + 1
                writeStr.append(St)

            def editName():
                tname = raw_input('Enter Name New: ')
                Str_new = Str.replace(name, tname)
                print Str_new
                writeStr.append(Str_new)
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
                fi = open('input.txt', 'w+')
                a = str(writeStr)
                a = a.lstrip('[')  # Xoa bo dau [] , ''
                a = a.rstrip(']')
                a = a.replace(",", "\n", k - 1)
                a = a.replace("'", "", k * 2)
                #print a
                fi.write(str(k) + '\n' + a)
                print 'Edited!'
                fi.close()

            print "Select: Edit Student"
            print "1. name: "
            print "2. SBD: "
            print "3. Add:"
            print "4. Sex:"
            print "0. Return"

            while True:
                try:
                    choice = (raw_input("Choose 0 -> 4: (press 0 to Return)"))
                    choice = int(choice)
                    if choice == 0:
                        print 'Return...'
                        StudentTmp.menu()
                        break
                    elif choice == 1:
                        print "1. Edit name: "
                        editName()
                        break
                    elif choice == 2:
                        print "2. Edit SBD "
                        # editId()
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
                        print("khong co lua chon nay ")
                except  ValueError:
                    print 'Nhap sai!!'
    def search(self):
        Students = StudentTmp.read_from_file()
        fo = open('timkiem.txt', 'a')  #mo file va ghi them vao cuoi file

        def tim_kiem_diem():
            k = 0
            aa = '\n\tResult tim kiem diem:\n'
            fo.write(aa)
            f=1
            while f ==1:
                try:
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
                            f = 0
                            #print 'saved!'
                except ValueError:
                    print 'Nhap sai diem'

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
            f=1
            while f==1:
                try:
                    tScore = float(raw_input('Nhap tong diem can tim: '))
                    Students = StudentTmp.read_from_file()
                    for Student in Students:

                        if ((float(Student['math']) + float(Student['physics']) + float(Student['chemistry'])) == tScore):
                            k = k+1
                            f=0
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
                except ValueError:
                    print 'Nhap sai diem!'

        print "Search Student:"
        print "1. theo tong so diem: "
        print "2. theo SBD: "
        print "3. theo Name"
        print "4. theo diem"
        print "0. Return"

        while True:
            try:
                choice = (raw_input("Choose 0 -> 4 (press 0 to return): "))
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
                print 'Error!!'

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
                    StudentTmp.menu()
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
