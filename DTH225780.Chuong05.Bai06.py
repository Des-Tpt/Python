import re

def NegativeNumberInStrings(s):
    negative_numbers = re.findall(r'-\d+', s)
    
    if negative_numbers:
        print("Các số nguyên âm trong chuỗi là:", negative_numbers)
    else:
        print("Không có số nguyên âm trong chuỗi.")

s = input("Nhập chuỗi: ")
NegativeNumberInStrings(s)
