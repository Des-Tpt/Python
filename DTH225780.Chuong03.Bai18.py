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

#Cái hình số 3 em chịu.