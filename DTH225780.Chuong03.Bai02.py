month = int(input("Nhập tháng (1-12): "))

if month == 2:
    year = int(input("Nhập năm: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Tháng 2 năm", year, "có 29 ngày.")
    else:
        print("Tháng 2 năm", year, "có 28 ngày.")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", month, "có 31 ngày.")
elif month in [4, 6, 9, 11]:
    print("Tháng", month, "có 30 ngày.")
else:
    print("Tháng không hợp lệ.")
