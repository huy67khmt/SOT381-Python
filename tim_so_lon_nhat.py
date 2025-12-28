# Nhập 3 số và in ra số lớn nhất.

number_one = int(input("Nhap vao so thu nhat: "))
number_two = int(input("Nhap vao so thu hai: "))
number_three = int(input("Nhap vao so thu ba: "))

bien_phu = 0

if number_one > number_two:
    bien_phu = number_one
    if number_three > bien_phu:
        bien_phu = number_three
elif number_two > number_three:
    bien_phu = number_two
else:
    bien_phu = number_three
    
print("So lon nhat la: ", bien_phu)


