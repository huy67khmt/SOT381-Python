# Kiểm tra số nhập vào là số nguyên tố.

number = int(input("Nhap vao mot so nguyen can kiem tra: "))
x = 0

for i in range(2, number-1):
    if number % i == 0:
        x += 1

if x > 0:
    print(f"so {number} khong phai la so nguyen to")
else:
    print(f"so {number} la so nguyen to")