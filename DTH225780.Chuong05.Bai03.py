def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

s = "5;7;8;-2;8;11;-13;9;10"

arr = s.split(';')

sochan = 0
soam = 0
sont = 0
sum = 0

for x in arr:
    print(x) 
    number = int(x) 

    if number % 2 == 0:
        sochan += 1

    if number < 0:
        soam += 1

    if CheckPrime(number):
        sont += 1

    sum += number


print("Tổng số chẵn: ", sochan)
print("Tổng số âm: ", soam)
print("Tổng số nguyên tố: ", sont)
print("Trung bình của chuỗi: ", sum / len(arr))
