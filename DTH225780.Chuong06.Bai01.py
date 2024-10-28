from random import randrange

print("Chương trình nhập List.")
n = int(input("Vui lòng nhập số phần tử trong List: "))
lst = [0] * n

for i in range (n):
    lst[i] = randrange(-100, 100)

print("List ngẫu nhiên là: ")
print(lst)
randomNumber = int(input("Mời bạn thêm một số bất kỳ vào list: "))
lst.append(randomNumber)
print(lst)

k = int(input("Vui lòng nhập số cần kiểm tra số lần xuất hiện: "))
dem = lst.count(k)
print(f"{k} xuất hiện {dem} lần trong list.")

def KtraSnt(n):
    d = 0
    for i in range (1, n+1):
        if n % i == 0:
            d += 1
    return d == 2

demnt = 0
tongnt = 0
for x in lst:
    if KtraSnt(x):
        demnt += 1
        tongnt += x

print(f"Có {demnt} số nguyên tố trong list.")
print(f"Tổng của các số nguyên tố trong list là: {tongnt}")

lst.sort()

print("List sau khi được sắp xếp là: ")
print(lst)

del lst
print("List đã được xóa!")