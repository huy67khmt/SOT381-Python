# Tìm số lớn nhất trong list.

lst = list(map(int,input("Nhap vao mot danh sach so: ").split()))
sln = 0

for i in range(len(lst)):
    if lst[i] > sln:
        sln = lst[i]

print(sln)