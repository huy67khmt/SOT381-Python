# Hiển thị bảng cửu chương (1–9).

def bangCuuChuong(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
    

number = int(input("Nhap vao bang cuu chuong muon hien thi: "))
bangCuuChuong(number)