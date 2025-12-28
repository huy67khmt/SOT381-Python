# Viết hàm trả về list các số nguyên tố < n.

def soNguyenTo(n):
    danh_sach = []
   
    for i in range(2, n):
        check = True
        for j in range(2, int(i**0.5) + 1):
           if i % j == 0:
               check = False
               break
        if check == True:
            danh_sach.append(i)
            
    return danh_sach

print(soNguyenTo(20))
                