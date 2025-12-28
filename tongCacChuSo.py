# Tính tổng các chữ số của một số nguyên

number = int(input("Nhap vao mot so nguyen: "))
sum = 0


while number > 0:
    sum = sum + int(number % 10)
    number = (int(number/10))
    
print(sum)