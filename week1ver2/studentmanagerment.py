class Student(object):
    def __init__(self, name, id_num, address, sex, maths, physics, chem):
        self.__name = name
        self.__id_num = id_num
        self.__address = address
        self.__sex = sex
        self.__maths = maths
        self.__physics = physics
        self.__chem = chem

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_idnum(self):
        return self.__id_num

    def set_idnum(self, id_num):
        self.__id_num = id_num

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex

    def get_maths(self):
        return self.__maths

    def set_maths(self, maths):
        self.__maths = maths

    def get_physics(self):
        return self.__physics

    def set_physics(self, physics):
        self.__physics = physics

    def get_chem(self):
        return self.__chem

    def set_chem(self, chem):
        self.__chem = chem

    def sum_mark(self):
        return self.__maths + self.__physics + self.__chem

    def print_info(self):
        print "ten         :", self.__name
        print "so bao danh :", self.__id_num
        print "dia chi     :", self.__address
        print "gioi tinh   :", self.__sex
        print "diem toan   :", self.__maths
        print "diem ly     :", self.__physics
        print "diem hoa    :", self.__chem


class StudentList(object):
    def __init__(self):
        self.__student_list = []
        self.__tmp_list = []

    def add_student(self):
        print "THEM SINH VIEN VAO DANH SACH"
        name = raw_input("ten : ")
        id_num = raw_input("so bao danh : ")
        address = raw_input("dia chi : ")
        sex = raw_input("gioi tinh : ")
        maths = float(raw_input("diem toan : "))
        physics = float(raw_input("diem ly : "))
        chem = float(raw_input("diem hoa : "))
        student = Student(name, id_num, address, sex, maths, physics, chem)
        self.__student_list.append(student)

    def edit_student_info(self):
        print "CAP NHAT THONG TIN SINH VIEN"
        pos = int(raw_input("Vi tri sinh vien trong danh sach: "))
        print "Thong tin moi: "
        name = raw_input("ten : ")
        id_num = raw_input("so bao danh : ")
        address = raw_input("dia chi : ")
        sex = raw_input("gioi tinh : ")
        maths = float(raw_input("diem toan : "))
        physics = float(raw_input("diem ly : "))
        chem = float(raw_input("diem hoa : "))
        student = Student(name, id_num, address, sex, maths, physics, chem)
        self.__student_list[pos - 1] = student

    def delete_student_info(self):
        print "XOA THONG TIN SINH VIEN"
        pos = int(raw_input("Vi tri sinh vien trong danh sach: "))
        for i in range(pos - 1, self.__student_list.__len__() - 1):
            j = i + 1
            self.__student_list[i] = self.__student_list[j]
        self.__student_list.pop()

    def get_data_from_keyboard(self):
        print "NHAP DU LIEU TU BAN PHIM"
        n = int(raw_input("So sinh vien: "))
        for i in range(0, n):
            print "Sinh Vien ", i + 1
            name = raw_input("ten : ")
            id_num = raw_input("so bao danh : ")
            address = raw_input("dia chi : ")
            sex = raw_input("gioi tinh : ")
            maths = float(raw_input("diem toan : "))
            physics = float(raw_input("diem ly : "))
            chem = float(raw_input("diem hoa : "))
            student = Student(name, id_num, address, sex, maths, physics, chem)
            self.__student_list.append(student)

    def get_data_from_file(self):
        print "NHAP DU LIEU TU FILE SAN CO"
        lnk = raw_input("Nhap vao duong dan file: ")
        f = open(lnk, 'a')
        f.readlines()
        f.close()

    def search_by_sum(self):
        mark = float(raw_input("Nhap vao tong diem sinh vien ban muon tim: "))
        for i in range(0, self.__student_list.__len__()):
            if self.__student_list[i].sum_mark() == mark:
                self.__student_list[i].print_info()
                self.__tmp_list.append(self.__student_list[i])
                print "Done!"

    def search_by_id(self):
        id_search = raw_input("Nhap vao so bao danh sinh vien ban muon tim kiem: ")
        for i in range(self.__student_list.__len__()):
            if self.__student_list[i].get_idnum() == id_search:
                self.__student_list[i].print_info()
                self.__tmp_list.append(self.__student_list[i])

    def search_by_name(self):
        name = raw_input("Nhap vao ten sinh vien ban muon tim: ")
        for i in range(self.__student_list.__len__()):
            if self.__student_list[i].get_name() == name:
                self.__student_list[i].print_info()
                self.__tmp_list.append(self.__student_list[i])

    def search_by_mark(self):
        subject = raw_input("Ban muon tim sinh vien theo diem mon gi (T/L/H): ")
        mark = float(raw_input("Nhap vao diem so ban muon tim: "))
        if subject == "t" or subject == "T":
            for i in range(self.__student_list.__len__()):
                if self.__student_list[i].get_maths() == mark:
                    self.__student_list[i].print_info()
                    self.__tmp_list.append(self.__student_list[i])
        elif subject == 'h' or subject == "H":
            for i in range(self.__student_list.__len__()):
                if self.__student_list[i].get_chem() == mark:
                    self.__student_list[i].print_info()
                    self.__tmp_list.append(self.__student_list[i])
        elif subject == "l" or subject == "L":
            for i in range(self.__student_list.__len__()):
                if self.__student_list[i].get_physics() == mark:
                    self.__student_list[i].print_info()
                    self.__tmp_list.append(self.__student_list[i])

    def sort_by_idnum(self):
        for i in range(self.__tmp_list.__len__()):
            j = i + 1
            if float(self.__tmp_list[i].get_idnum()) > float(self.__tmp_list[j].get_idnum()):
                self.__tmp_list[i], self.__tmp_list[j] = self.__tmp_list[j], self.__tmp_list[i]

    def sort_by_sum(self):
        for i in range(self.__tmp_list.__len__() - 1):
            j = i + 1
            if self.__tmp_list[i].sum_mark() > self.__tmp_list[j].sum_mark():
                self.__tmp_list[i], self.__tmp_list[j] = self.__tmp_list[j], self.__tmp_list[i]


    def write_to_file(self):
        lnk = raw_input("Nhap duong dan de luu file: ")
        f = open(lnk, 'w')
        tmp = " "
        for student in self.__tmp_list:
            tmp += student.print_info()
            tmp += "\n"
        f.write(tmp)
        f.close()


if __name__ == "__main__":
    list1 = StudentList()
    while True:
        print "CHUONG TRINH QUAN LY DIEM THI"
        print "Moi lua chon chuc nang"
        print "1. Them thong tin sinh vien"
        print "2. Thay doi thong tin sinh vien"
        print "3. xoa thong tin sv"
        print "4. Nhap du lieu tu ban phim"
        print "5. Nhap du lieu tu file"
        print "6. Tim kiem theo tong diem"
        print "7. Tim kiem theo so bao danh"
        print "8. Tim kiem theo ten"
        print "9. Tim kiem theo diem tung mon"
        print "10.Sap xep theo so bao danh"
        print "11.Sap xep theo tong diem"
        print "12.Luu ket qua tim kiem"
        key = int(raw_input())
        if key == 1:
            list1.add_student()
        elif key == 2:
            list1.edit_student_info()
        elif key == 3:
            list1.delete_student_info()
        elif key == 4:
            list1.get_data_from_keyboard()
            pass
        elif key == 5:
            list1.get_data_from_file()
        elif key == 6:
            list1.search_by_sum()
        elif key == 7:
            list1.search_by_id()
        elif key == 8:
            list1.search_by_name()
        elif key == 9:
            list1.search_by_mark()
        elif key == 10:
            list1.sort_by_idnum()
        elif key == 11:
            list1.sort_by_sum()
        elif key == 12:
            list1.write_to_file()
