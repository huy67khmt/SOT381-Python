# Tính giai thừa của một số.

number = int(input("Nhap vao mot so nguyen: "))
giai_thua = 1

for i in range(1, number + 1):
    giai_thua *= i
    
print("gia thua cua number la: ", giai_thua)