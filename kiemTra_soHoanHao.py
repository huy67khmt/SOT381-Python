# Viết hàm kiểm tra số hoàn hảo.

def checkSoHoanHao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        print(f"{n} la so hoan hao")
    else:
        print(f"{n} khong phai la so hoan hao")
    
number = int(input("Nhap vao so nguyen can kiem tra co phai la so nguyen to hay khong: "))
checkSoHoanHao(number)
