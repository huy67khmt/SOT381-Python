# Nhập n, tìm chữ số lớn nhất của n

n = int(input("Nhap vao n: "))
n = abs(n)

chu_so_lon_nhat = 0

while n > 0: 
    if n % 10 > chu_so_lon_nhat:
        chu_so_lon_nhat = n % 10
    n //= 10

print (chu_so_lon_nhat)