from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))  # Tạo số ngẫu nhiên từ 0 đến 99 theo cột
        D.append(row)
    return D

# Xuất ma trận ra màn hình
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()  # Xuống dòng sau khi in xong mỗi hàng

# Lấy dòng thứ r của ma trận
def LayDong(D, row):
    R = D[row]
    return R

# Xuất danh sách một chiều (ví dụ: dòng hoặc cột)
def XuatList1Chieu(L):
    for element in L:
        print(element, end='\t')
    print()  # Xuống dòng sau khi in xong

# Lấy cột thứ c của ma trận
def LayCot(D, coluum):
    C = []
    for i in range(len(D)):
        C.append(D[i][coluum])
    return C

# Tìm giá trị lớn nhất trong ma trận
def MAX(D):
    max_value = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_value < D[i][j]:
                max_value = D[i][j]
    return max_value

# Chương trình chính
print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

# Tạo và xuất ma trận
D = TaoMaTran(m, n)
print("Ma trận được tạo ngẫu nhiên là:")
XuatMaTran(D)

# Nhập và xuất dòng mong muốn
print("Mời bạn nhập dòng muốn xuất:")
r = int(input())
print(f"Dòng {r} trong ma trận là:")
XuatList1Chieu(LayDong(D, r))

# Nhập và xuất cột mong muốn
print("Mời bạn nhập cột muốn xuất:")
c = int(input())
print(f"Cột {c} trong ma trận là:")
XuatList1Chieu(LayCot(D, c))

# Tìm và in số lớn nhất trong ma trận
max_value = MAX(D)
print("Số lớn nhất trong ma trận =", max_value)
