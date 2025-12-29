

n = int(input("nhap vao n: "))
tong = 0

for i in range(1, n + 1):
    tong += (1/(i *(i+1)))
    
print(tong)