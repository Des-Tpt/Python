def NhapVaSapXepDayGiamDan():
    n = int(input("Nhập số lượng phần tử: "))
    M = []
    for i in range(n):
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        M.append(x)
    M.sort(reverse=True)
    return M

day_giam_dan = NhapVaSapXepDayGiamDan()
print("Dãy số theo thứ tự giảm dần là:", day_giam_dan)
