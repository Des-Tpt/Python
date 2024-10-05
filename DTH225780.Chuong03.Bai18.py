n = int(input("Nhập chiều cao n: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * n) 
    else:
        print('* ' + '  ' * (n - 2) + '*')


n = int(input("Nhập chiều cao n: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print('* ' * (i + 1))
    else:
        print('* ' + '  ' * (i - 1) + '*')

def test(n3):
    for i in range(n3):
        if i == n3 // 2:
            print("*"*n3)
        else:
            if i < n3 // 2 and i != 0:
                print("*" + " " * (i-1) + "*")
            elif i > n3 // 2 and i != n3 - 1:
                print(" " * i + "*" + " " * (n3 - (i+2)) + "*")
            else:
                print(" " * i + "*")
test(7)
        