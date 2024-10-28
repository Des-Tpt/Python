from random import randrange

def TaoListKhongTrung(n):
    lst = set()
    while len(lst) < n:
        lst.add(randrange(100)) 
    return list(lst)

n = int(input("Nhập số lượng phần tử: "))
list_khong_trung = TaoListKhongTrung(n)
print("List có các phần tử ngẫu nhiên không trùng nhau:", list_khong_trung)
