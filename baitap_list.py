lst = list(map(int, input("Nhap vao so nguyen cach nhau bang dau cach: ").split()))

# Tìm số lớn nhất trong list.
max = 0
for i in range(0, len(lst)):
    if int(lst[i]) > max:
        max = lst[i]
print("so lon nhat trong list la: ", max)

# Tính trung bình của các phần tử trong list.
sum = 0
for i in range(0, len(lst)):
    sum += lst[i]
trung_binh = int(sum / len(lst))

print("So trung binh cua list la: ", trung_binh)

# Loại bỏ phần tử trùng lặp khỏi list.

for i in range(0, len(lst)):
    bien_dem = 0
    for j in range(0, len(lst)):
        if lst[i] == lst[j]:
            bien_dem += 1
    if bien_dem > 1:
        lst.remove(lst[i])
print(lst)