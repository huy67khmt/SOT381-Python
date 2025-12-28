# Tính trung bình của các phần tử trong list.

n = int(input("Nhap so phan tu co trong list: "))
lst = []
tong = 0

for i in range(0, n):
    x = int(input(f"nhap vao gia tri cho list tai vi tri {i}: "))
    lst.append(x)
    tong += x
trung_binh = float(tong / n)

print(trung_binh)    


