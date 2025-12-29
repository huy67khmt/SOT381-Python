diem_toan = float(input("Nhap vao diem toan: "))
diem_hoa = float(input("Nhap vao diem hoa: "))
diem_ly = float(input("Nhap vao diem ly: "))

tong_diem = diem_toan + diem_hoa + diem_ly

if tong_diem >= 15:
    if diem_toan >= 4 and diem_hoa >= 4 and diem_ly >= 4:
        print("Thi dau")
        if diem_toan > 5 and diem_hoa > 5 and diem_ly > 5:
            print("Hoc deu cac mon")
        else:
            print("Hoc chua deu cac mon")
    else:
        print("Thi hong")
else:
    print("Thi hong")