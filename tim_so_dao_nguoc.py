# Nhập n, tìm số đảo ngược rồi kiểm tra có chia hết cho 9 không.

n = int(input("Nhap vao so n: "))
n = abs(n)

n_nguoc = 0
bien_phu = n

while bien_phu > 0:
   n_nguoc = n_nguoc * 10 + bien_phu % 10
   bien_phu //= 10

n_nguoc = int(n_nguoc)
print(n_nguoc)
if n_nguoc % 9 == 0:
    print(f"{n_nguoc} chia het cho 9")
else: print(f"{n_nguoc} khong chia het cho 9")