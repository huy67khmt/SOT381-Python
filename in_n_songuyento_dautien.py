# Nhập n, in ra n số nguyên tố đầu tiên.

n = int(input("Nhap vao n: "))
dem = 0
lon_nhat, start = 2

while dem < n:
    so_nguyen_to = True
    for i in range(2, start//2 + 1):
        if start % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to == True: 
        print(f"{start} la so nguyen to")
        dem += 1
    start += 1
    