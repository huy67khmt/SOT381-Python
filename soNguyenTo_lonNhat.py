# Nhập n, tìm số nguyên tố lớn nhất nhỏ hơn n.

n = int(input("Nhap vao so n: "))
so_LN = 0

for i in range(2, n):
    check = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            check = False
            break
    if check:
        if i > so_LN:
            so_LN = i

print(f"{so_LN} la so nguyen to lon nhat nho hon {n}")