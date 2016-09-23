Chuong trinh chinh: Solution.py
su dung python version 2.7
file input: input.txt
file output: output.txt
--
1. Đọc và xuất thông tin Studenàn t ra màn hình
2. Nhập thông tin cho n SV từ bàn phím
    Nhạp n:
    Nhập thong tin cho sv i+1:
    	name, add, sex, math, physics, chemistry (id k được nhập, id = k+i+1)
    nhap xong thi luu de vao file ban dau (input.txt)
    total = total + n

3.  Edit 
	lay all Students trong input.txt ra
	nhap id student can sua 
	neu co id thi remove khoi Students
	luu Students con lai vao []
	--
	dung replace de Edit
	Edit xong thi append vao []
	ghi de [] vao input.txt
4. Delete
	lay all Students trong input.txt ra
	nhap id student can xoa 
	neu co id thi remove khoi Students
	luu Students con lai vao []
	ghi de [] vao input.txt
5. tim kiem
	lay all Students trong input.txt ra
	nhap value can tim
	kiem tra xem student['key'] == value?
	neu co Student thoa man thi save append vao file output.txt

6. thong ke 
	tuong tu nhu tim kiem
	tinh tong diem 3 mon thoa man dieu kien thi append vao []
	cho bien k dem Student thoa man 
	save k va [] vao file thongke.txt



-
Chưa xử lý hết lỗi ngoại lệ
thao tác với file chưa thạo r, r+, w, w+, a, a+


