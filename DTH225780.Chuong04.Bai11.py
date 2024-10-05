def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s  # Kết quả trả về là n

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s  # Kết quả trả về là giá trị ban đầu của val

def sum3():
    global val
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s  # Kết quả trả về là giá trị ban đầu của val

#Trường hợp 1:

def main():
    global val
    val = 5
    print(sum1(5))  # Kết quả là 5
    print(sum2())   # Kết quả là 5, val giảm xuống 0
    print(sum3())   # Kết quả là 0, val đã là 0 trước đó, vì val là biến toàn cục
main()

#Trường hợp 2:

def main():
    global val
    val = 5
    print(sum1(5))  # Kết quả là 5
    print(sum3())   # Kết quả là 5, val vẫn là 5
    print(sum2())   # Kết quả là 5, val giảm xuống 0
main()

#Trường hợp 3:

def main():
    global val
    val = 5
    print(sum2())   # Kết quả là 5, val giảm xuống 0
    print(sum1(5))  # Kết quả là 5
    print(sum3())   # Kết quả là 0, val đã là 0 trước đó
main()
