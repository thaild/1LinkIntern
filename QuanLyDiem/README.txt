Chuong trinh chinh: Solution.py
su dung python version 2.7
file input: input.txt
file output: output.txt
file thongke.txt -> luu ket qua thong ke
file timkiem.txt -> luu ket qua tim kiem
--
1. Đọc và xuất thông tin Students ra màn hình
2. Nhập thông tin cho n SV từ bàn phím
    Nhạp n: ()
    Nhập thong tin cho sv i+1: (vì i trong for i in range(n) tính từ 0)
    	name, add, sex, math, physics, chemistry (id k được nhập, id = k+i+1)
    nhap xong thi luu vao file ban dau (input.txt)
    dùng phưong thức ghi đè file
    total = total + n


3.  Edit 
	nhap ID: 
	lay all Students trong input.txt ra
	kiểm tra xem có id nào trùng vs id mới nhập k? 
	neu co id thi remove student có id đó khỏi Students
	luu Students con lai vao []
	--
	dung replace de Edit
	Edit xong thi append student vao Students
	ghi đè Students [] vao input.txt

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

--
phần sort chưa chuẩn,
@@
see code cứ bị ngu ngu @@

