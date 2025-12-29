# A1. CHƯƠNG TRÌNH XẾP LOẠI ĐIỂM
# Viết chương trình nhập vào điểm trung bình của một học sinh (số thực từ 0 đến 10).
# Xếp loại học sinh theo quy tắc sau và in ra kết quả:

dtb = float(input("Nhap vao diem trung binh cua hoc sinh: "))
xep_loai = ""

if dtb < 0 or dtb > 10:
    print("Diem nhap vao khong hop le")
else:
    if dtb >= 8:
       xep_loai = "Giỏi"
    if dtb >= 6.5 and dtb < 8:
       xep_loai = "Khá"
    if dtb >= 5.0 and dtb < 6.5:
       xep_loai = "Trung Bình"
    if dtb >= 3.5 and dtb < 5:
       xep_loai = "Yếu"
    if dtb < 3.5:
       xep_loai = "Kém"
       
print(f"xep loai cua hoc sinh la: {xep_loai}")