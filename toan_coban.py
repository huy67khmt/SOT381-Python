# Nhập hai số và in ra tổng, hiệu, tích, thương.

number1 = float(input("Nhap vao so thu nhat: "))
number2 = float(input("Nhap vao so thu hai: "))


tong = number1 + number2
hieu = number1 - number2
tich = number1 * number2
thuong = number1 / number2
du = number1 % number2
luy_thua = number1 ** number2

print(f"Tong cua {number1} va {number2} la {tong}")
print(f"hieu cua {number1} va {number2} la {hieu}")
print(f"tich cua {number1} va {number2} la {tich}")
print(f"thuong cua {number1} va {number2} la {thuong}")
print(f"du cua {number1} va {number2} la {du}")
print(f"luy thua cua {number1} va {number2} la {luy_thua}")
