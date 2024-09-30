ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    ngay_trong_thang[1] = 29 

ngay += 1

if ngay > ngay_trong_thang[thang - 1]:
    ngay = 1
    thang += 1

if thang > 12:
    thang = 1
    nam += 1

print(f"Ngày kế tiếp là: {ngay}/{thang}/{nam}")
