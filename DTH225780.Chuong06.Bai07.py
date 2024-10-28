def NhapDayTangDan():
    d = []
    n = int(input("Nhập số lượng phần tử: "))
    for i in range(n):
        while True:
            x = float(input(f"Nhập phần tử thứ {i+1}: "))
            if i == 0 or x > d[-1]:
                d.append(x)
                break
            else:
                print("Phần tử phải lớn hơn phần tử trước đó. Nhập lại.")
    return d

day_tang_dan = NhapDayTangDan()
print("Dãy số theo thứ tự tăng dần là:", day_tang_dan)
