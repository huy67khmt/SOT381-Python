import math
x = float(input("Nhap vao x: "))
n = int(input("Nhap vao n: "))
ket_qua = 0
ket_qua_2 = 1 

for i in range(1, n + 1):
    ket_qua = math.sqrt(x + ket_qua)
    
for i in range(1, n + 1):
    ket_qua_2 += ((x**i)/(i+1))

print(ket_qua)
print(ket_qua_2)

