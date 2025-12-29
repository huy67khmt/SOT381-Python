n = int(input("Nhap vao so luong phan tu: "))
lst = []
dem = 0
for i in range(0, n):
    x = int(input("Nhap vao gia tri: "))
    lst.append(x)
    
for i in range(0, n): 
    if lst[i] % 2 == 0:
       dem += 1
       
print(f"so luong phan tu co gia tri chan la: {dem}")