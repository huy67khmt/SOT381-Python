def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


n = int(input("Nhap vao so luong phan tu: "))
lst = []
dem = 0

for i in range(0, n):
    x = int(input(f"Nhap vao gia tri tai vi tri {i}: "))
    lst.append(x)
    
for i in range(0, n):
    if is_prime(lst[i]):
        print(lst[i])
        dem += 1

print(f"so luong so nguyen to la {dem}")