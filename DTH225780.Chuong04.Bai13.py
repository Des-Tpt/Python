def Tong_Uoc_So(n):
    total = 0
    for i in range(1, n // 2 + 1): 
        if n % i == 0:
            total += i
    return total

def Ktr_So_Hoan_Thien(n):
    return Tong_Uoc_So(n) == n

def Ktr_So_Thinh_Vuong(n):
    return Tong_Uoc_So(n) > n

n = int(input("Nhập số nguyên dương n: "))

if Ktr_So_Hoan_Thien(n):
    print(f"{n} là số hoàn thiện.")
else:
    print(f"{n} không phải là số hoàn thiện.")

if Ktr_So_Thinh_Vuong(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không phải là số thịnh vượng.")
