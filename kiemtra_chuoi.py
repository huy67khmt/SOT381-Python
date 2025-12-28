# Kiểm tra chuỗi có bắt đầu bằng một ký tự cho trước không.

s_nhap_vao = input("Nhap vao mot chuoi bat ky: ")
check_word = input("nhap vao mot ky tu kiem tra: ")

if s_nhap_vao[0] == check_word:
    print(f"chuoi {s_nhap_vao} duoc bat dau bang ky tu {check_word}")
else: 
    print(f"chuoi {s_nhap_vao} khong duoc bat dau bang ky tu {check_word}")