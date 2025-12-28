number = int(input("Nhap vao mot so nguyen: "))
sum = 0

for i in range(1,number + 1):
    if i % 3 != 0 and i % 5 !=0:
        sum += i
        
print("Tong cac so nguyen khong chia het cho 3 va 5 la: ", sum)