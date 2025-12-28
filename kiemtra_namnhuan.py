# Kiểm tra năm nhuận.

year = int(input("nhap vao nam can kiem tra: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} la nam nhuan")
elif year % 400 == 0:
    print(f"{year} la nam nhuan")
else:
    print(f"{year} khong phai la nam nhuan")