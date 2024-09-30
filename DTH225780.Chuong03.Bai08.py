a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phep_toan = input("Nhập phép toán (+, -, *, /): ")

if phep_toan == '+':
    ket_qua = a + b
    print(f"Kết quả: {a} + {b} = {ket_qua}")
elif phep_toan == '-':
    ket_qua = a - b
    print(f"Kết quả: {a} - {b} = {ket_qua}")
elif phep_toan == '*':
    ket_qua = a * b
    print(f"Kết quả: {a} * {b} = {ket_qua}")
elif phep_toan == '/':
    if b != 0:
        ket_qua = a / b
        print(f"Kết quả: {a} / {b} = {ket_qua}")
    else:
        print("Lỗi: Không thể chia cho 0.")
else:
    print("Lỗi: Phép toán không hợp lệ.")
