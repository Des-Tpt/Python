def CheckDoiXung(s):
    flag = True
    for i in range(len(s) // 2):  # Chỉ cần so sánh nửa đầu với nửa cuối, vì bản chứng của chuỗi đối xứng.
        if s[i] != s[len(s) - i - 1]: # VD: Strong. Len(s) là 5, nếu i = 0, s[i] = S và s[5 - 0 - 1] = g. 
            flag = False
            break
    return flag

def main():
    print("Nhập 1 chuỗi:")
    s = input()
    if CheckDoiXung(s):
        print("Chuỗi bạn nhập đối xứng")
    else:
        print("Chuỗi bạn nhập không đối xứng")

while True:
    main()
    print("Tiếp không Thím? (c/k):")
    s = input()
    if s.lower() == "k":
        break

print("CÁM ƠN NÍ")
