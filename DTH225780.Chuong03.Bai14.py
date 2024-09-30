a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1
    '''
Với mỗi giá trị a, vòng lặp b sẽ chạy từ 0 đến 39 (tức là 40 lần).
Điều kiện (a + b) % 2 == 0 sẽ thỏa mãn khi tổng a + b là số chẵn, nghĩa là có một nửa số lần lặp b sẽ thỏa mãn điều kiện này (20 lần).
Vì vòng lặp ngoài chạy 100 lần, và mỗi lần vòng lặp trong in ra 20 dấu *, tổng số dấu * in ra là: 100×20=2000

    '''
