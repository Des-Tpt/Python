def la_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

so_le = []
so_chan = []
so_nguyen_to = []
so_khong_phai_nguyen_to = []

for num in M:
    if num % 2 != 0:
        so_le.append(num)
    else:
        so_chan.append(num)

    if la_so_nguyen_to(num):
        so_nguyen_to.append(num)
    else:
        so_khong_phai_nguyen_to.append(num)

print("Dòng 1: Số lẻ:", so_le, f"({len(so_le)} số lẻ)")
print("Dòng 2: Số chẵn:", so_chan, f"({len(so_chan)} số chẵn)")
print("Dòng 3: Số nguyên tố:", so_nguyen_to)
print("Dòng 4: Số không phải nguyên tố:", so_khong_phai_nguyen_to)
