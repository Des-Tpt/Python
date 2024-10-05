import math

def S(x, n):
    result = 0
    for i in range(n+1):
        term = x**(2*i+1) / math.factorial(2*i+1)
        result += term
    return result

x = int(input("Nhập x:"))
n = int(input("Nhập n: "))
Ketqua = S(x, n)

print(f"Đáp án: {Ketqua}")
