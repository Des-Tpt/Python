def XuLyChuoi(s):
    in_hoa = 0
    in_thuong = 0
    chu_so = 0
    ky_tu_dac_biet = 0
    khoang_trang = 0
    nguyen_am = 0
    phu_am = 0
    
    Danh_sanh_nguyen_am = "AOEUIaoeui"
    
    for char in s:
        if char.isupper(): 
            in_hoa += 1
        elif char.islower():  
            in_thuong += 1
        elif char.isdigit():  
            chu_so += 1
        elif char.isspace():  
            khoang_trang += 1
        else:  
            ky_tu_dac_biet += 1
        
        if char in Danh_sanh_nguyen_am:
            nguyen_am += 1

        elif char.isalpha():
            phu_am += 1
    
    print(f"Số chữ IN HOA: {in_hoa}")
    print(f"Số chữ in thường: {in_thuong}")
    print(f"Số chữ là chữ số: {chu_so}")
    print(f"Số ký tự đặc biệt: {ky_tu_dac_biet}")
    print(f"Số ký tự khoảng trắng: {khoang_trang}")
    print(f"Số chữ Nguyên Âm: {nguyen_am}")
    print(f"Số chữ Phụ Âm: {phu_am}")

s = input("Nhập chuỗi: ")
XuLyChuoi(s)
