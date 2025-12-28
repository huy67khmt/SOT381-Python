# Nhập n, đếm số chữ số lẻ trong n

n = abs(int(input("Nhap vao n: ")))

bien_dem = 0
while True: 
    if (n % 10) % 2 != 0:
        bien_dem += 1
    n //= 10
    if n == 0: 
        break
print(bien_dem)
