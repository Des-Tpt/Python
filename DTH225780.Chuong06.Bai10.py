def nhap_ma_tran(m, n):
    ma_tran = []
    for i in range(m):
        hang = list(map(int, input(f"Nhập dòng {i + 1} (các số cách nhau bởi dấu cách): ").split()))
        while len(hang) != n:
            hang = list(map(int, input(f"Nhập dòng {i + 1} (các số cách nhau bởi dấu cách): ").split()))
        ma_tran.append(hang)
    return ma_tran

def in_ma_tran(mat):
    for row in mat:
        print("\t".join(map(str, row)))

def cong_ma_tran(A, B):
    m = len(A)
    n = len(A[0])
    C = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def hoan_vi(mat):
    return [list(row) for row in zip(*mat)]

print("Nhập ma trận A:")
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
A = nhap_ma_tran(m, n)

print("Nhập ma trận B:")
B = nhap_ma_tran(m, n)

C = cong_ma_tran(A, B)
print("Ma trận A + B là:")
in_ma_tran(C)

print("Hoán vị của ma trận A là:")
in_ma_tran(hoan_vi(A))

print("Hoán vị của ma trận B là:")
in_ma_tran(hoan_vi(B))
