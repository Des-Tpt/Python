import math

def loga_x(x, a):
    return math.log(x) / math.log(a)

x = float(input("Nhập x (x > 0): "))
a = float(input("Nhập a (a > 0 và khác 1): "))

if x <= 0:
    print("Giá trị x phải lớn hơn 0.")
elif a <= 0 or a == 1:
    print("Giá trị a phải lớn hơn 0 và không bằng 1.")
else:
    result = loga_x(x, a)
    print(f"log_{a}({x}) = {result}")
