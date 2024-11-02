import csv
import random

def tao_csv(ten_tap_tin):
    with open(ten_tap_tin, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(10):
            dong = [random.randint(0, 100) for _ in range(10)]
            writer.writerow(dong)

def doc_va_tinh_tong(ten_tap_tin):
    with open(ten_tap_tin, mode='r') as file:
        reader = csv.reader(file)
        for chi_so, dong in enumerate(reader):
            gia_tri_dong = list(map(int, dong))
            tong_dong = sum(gia_tri_dong)
            print(f"Tổng các giá trị trong dòng {chi_so + 1}: {tong_dong}")

ten_tap_tin = 'so_ngau_nhien.csv'
tao_csv(ten_tap_tin)
doc_va_tinh_tong(ten_tap_tin)
