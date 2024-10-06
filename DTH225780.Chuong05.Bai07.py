def ToiUuChuoiDanhTu(s):
    s = s.strip()

    arr = s.split()

    Toi_uu_cac_tu = [word.capitalize() for word in arr]
    
    Toi_uu_cac_tu = ' '.join(Toi_uu_cac_tu)
    
    return Toi_uu_cac_tu

input_string = input("Nhập chuỗi danh từ: ")
output_string = ToiUuChuoiDanhTu(input_string)
print("Chuỗi tối ưu:", output_string)
