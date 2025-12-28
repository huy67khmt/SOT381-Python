# Tính tổng các số từ 1 → n.

number = int(input("Nhap vao mot so nguyen: "))
sum = 0

for i in range(1, number + 1):
    sum += i
print("tong tu 1 den number la: ", sum)

