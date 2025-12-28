# Kiểm tra số nhập vào là chẵn hay lẻ.

number = int(input("Nhap vao mot so nguyen: "))

if number % 2 == 0:
    print(f"so {number} la so chan")
else:
    print(f"so {number} la so le")