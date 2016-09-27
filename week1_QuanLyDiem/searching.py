from solution import *

def editStudent(self):
    Students = StudentTmp.read_from_file()
    fo = open('input.txt', 'a')
    key = raw_input('Nhap id Student can sua: ')

    def editName():
        for Student in Students:
            if (Student['id'] == key):
                s = Student['name'] + ' ' + Student['id'] + ' ' + Student['add'] + ' ' + Student['sex'] + ' ' + \
                    Student['math'] + ' ' + Student['physics'] + ' ' + Student['chemistry']
            print s
            tname = raw_input('Edit ',Student['name'],': ')

            writeStr = []
            writeStr.append(s)

            a = str(writeStr) + 'edited\n'
            print a
            #fo.write(a)

    print "Edit Student:"
    print "1. Edit name: "
    print "2. Edit SBD: "
    print "3. Edit Sex:"
    print "4. Edit add:"
    print "5. Edit Math:"
    print "6. Edit Physics:"
    print "7. Edit Chemistry:"
    print "0. Return"

    var = 1
    while var == 1:
        choice = (raw_input("Nhap lua chon 0 -> 7: "))
        choice = int(choice)
        if choice == 0:
            print 'Return...'
            StudentTmp.menu()
        elif choice == 1:
            print "1. Edit name: "
            editName()
        elif choice == 2:
            print "2. Edit SBD "

        elif choice == 3:
            print "3. Edit Sex"

        elif choice == 4:
            print "4. Edit Add"
        elif choice == 5:
            print "5. Edit Math"
        elif choice == 6:
            print "6. Edit Physics"
        elif choice == 7:
            print "7. Edit chemistry"

        else:
            print("khong co lua chon nay ")



if __name__ == '__main__':
    StudentTmp = Student('name','id', 'add', 'sex', 0,0,0)
    StudentTmp.editStudent()