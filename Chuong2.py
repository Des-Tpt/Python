# Cau 1:
import math

try: 
    r = float (input("Mời bạn nhập bán kính hình tròn: "))
    cv = 2*math.pi*r
    dt = r*r*math.pi
    print("Chu vi =", cv)
    print("Diện tích =", dt)
except:
    print("Lỗi rồi!")

# Cau 2:
t = int (input("Nhập số giây: "))
hour = (t//3600) % 12
check = (t//3600) // 12
min = (t%3600) // 60
second = (t%3600) % 60

if (check % 2 == 0): 
    time = "AM"
else: 
    time = "PM"
print (hour, ":", min, ":", second, time) 

# Câu 3: 

toan, ly, hoa = eval (input("Nhập điểm toán lý hóa: "))
print("Điểm toán: ", toan)
print("Điểm hóa: ", hoa)
print("Điểm lý: ", ly)

dtb = (toan + ly + hoa) / 3;
round_dtb = round (dtb, 2)

print ("Điểm trung bình: ", round_dtb)

print("Câu 4:")
print("Python hỗ trợ các kiểu dữ liệu cơ bản: int, float, complex, str, list, tuple, range, dict, set, frozen set, bool, byte, bytearray, memoryview.")
print("Câu 5:")
print("Các loại ghi chú trong Python:" )
print("-Dạng Comment với dấu # ở đầu dòng: # This is a comment.")
print("-Dạng Block Comment, tức một tập hợp các chuỗi Comment: # The main function  # This is a comment  # This is another comment # This is another comment again")
print("-Dạng ghi chú trên các dòng lệnh: [code] # This is a description about the code.")
print("-Dạng Comment out code để thử nghiệm: [import random  number = random.randint(1, 25] # This is a comment about the random function.")
print("Ngoài ra có thể dùng dấu ''' Note ''' để ghi chú nhiều dòng.")
''' Câu 6:
//	Thực hiện phép chia, tròng đó kết quả là những thương số  sau khi đã xóa các chữ số sau dấu phẩy
+	Phép cộng
-	Phép trừ
*	Phép nhân
/ 	phép chia
%	Phép chia lấy phần dư
**	Phép lấy số mũ (ví dụ 2**3 cho kết quả bằng 8)

        Câu 7:
    Sử dụng hàm input. Ví dụ:
    '''
print("Vui lòng nhập một số bất kỳ: ")
s = input();
print("Số bạn vừa nhập là: ",s)

'''
    Câu 8: 
    Các lỗi thường gặp: 
    -Lỗi cú pháp.
    -Lỗi thực thi.
    -Lỗi đánh giá.

    Ta có thể dùng Python Debugger để bắt lỗi.

    Câu 9: 
    Cách thực hiện: Python sẽ thực hiện phép toán theo thứ tự, các phép toán trong ngoặc,
    phép nhân chia, rồi sau cùng là phép cộng trừ. Nếu cùng bật, thực hiện từ trái sang 
    phải:   
'''
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

print("a: ", i1 + (i2 * i3))
print("b: ", i1 - (i2+i3))
print("c: ", i1 / (i2 + i3))
print("d: ", i1 // (i2 + i3))
print("e: ", i1 / i2 + i3)
print("f: ", i1 // i2 + i3)
print("g: ", 3 + 4 + 5 / 3)
print("h: ", 3 + 4 + 5 // 3)
print("j: ", (3 + 4 + 5) / 3)
print("i: ", (3 + 4 + 5) // 3)
print("k: ", d1 + (d2 * d3))
print("l: ", d1 + d2 * d3)  
print("m: ", d1 / d2 - d3)
print("n: ", d1 / (d2 - d3))
print("o: ", d1 + d2 + d3 /3)
print("p: ", (d1 + d2 + d3) /3)
print("q: ", d1 + d2 + (d3 /3))
print("r: ", 3 * (d1 + d2) * (d1 - d3))
       