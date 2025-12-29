n = int(input("Nhap vao so luong phan tu: "))
lst = []
tong = 0
for i in range(0, n):
    x = int(input(f"Nhap vao gia tri tai vi tri {i}: "))
    lst.append(x)

for i in range(0, n):
    if i % 2 == 0:
        tong+= lst[i]
        
print(tong)