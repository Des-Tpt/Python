import math

def Canbac2Longnhau(n):
    result = 0
    for _ in range(n):
        result = math.sqrt(2 + result)
    return result

n = int(input("Nhập n: "))
print(f"S(n) = {Canbac2Longnhau(n)}")
