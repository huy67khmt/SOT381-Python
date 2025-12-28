# Thay thế tất cả khoảng trắng bằng dấu gạch dưới _.

s_nhap_vao = input("Nhap vao mot chuoi bat ky: ")
new_string = ""

print(s_nhap_vao)

for i in range(0, len(s_nhap_vao)):
    if s_nhap_vao[i] == " ":
        new_string += "_"
    else:
        new_string += s_nhap_vao[i]

print(new_string)