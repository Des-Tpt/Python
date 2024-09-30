hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

n = int(input("Nhập số n có tối đa 2 chữ số: "))

if 0 <= n < 100:
    if n < 10:
        if n == 0:
            print("không")
        else:
            print(hang_don_vi[n])
    else:
        chuc = n // 10
        don_vi = n % 10

        if don_vi == 0:
            print(hang_chuc[chuc])
        elif don_vi == 5 and chuc != 0:
            print(hang_chuc[chuc] + " lăm")
        elif chuc == 1:
            if don_vi == 5:
                print("mười lăm")
            else:
                print("mười " + hang_don_vi[don_vi])
        else:
            print(hang_chuc[chuc] + " " + hang_don_vi[don_vi])
else:
    print("Vui lòng nhập số có tối đa 2 chữ số.")
