def ToiUuChuoi(s):
    s2 = s
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    s2 = s2.strip()
    print(s2)

    # Tách chuỗi thành các từ bằng dấu space
    arr = s2.split(' ')
    print(arr)

    # Xây dựng lại chuỗi, bỏ qua các khoảng trắng dư thừa
    s2 = ""
    for word in arr:
        if len(word.strip()) != 0:  # Loại bỏ từ rỗng hoặc khoảng trắng
            s2 += word + " "
    
    return s2.strip()

# Chuỗi đầu vào
s = "  Đào   Duy Thanh   "
print(s, "=>", len(s))

# Gọi hàm tối ưu chuỗi
s = ToiUuChuoi(s)
print(s, "=>", len(s))
