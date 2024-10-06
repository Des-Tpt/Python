'''
    len(): Tính độ dài chuỗi.
    strip(): Xóa bỏ các khoảng trắng thừa ở đầu và cuối chuỗi.
    lstrip(): Xóa bỏ khoảng trắng ở đầu chuỗi.
    rstrip(): Xóa bỏ khoảng trắng ở cuối chuỗi.
    split(): Tách chuỗi thành danh sách.
    join(): Ghép các phần tử của danh sách thành chuỗi.
    replace(): Thay thế chuỗi con.
        -Vd:    new_s = s.replace("World", "Python")
                print(new_s)  # Output: "Hello Python"
    upper(): Chuyển chuỗi thành chữ in hoa.
    lower(): Chuyển chuỗi thành chữ thường.
    capitalize(): Viết hoa chữ cái đầu tiên của chuỗi.
    find(chuỗi con): Tìm vị trí xuất hiện đầu tiên của chuỗi con, trả về -1 nếu không tìm thấy.
    index(chuỗi con): Tương tự như find(), nhưng sẽ báo lỗi nếu không tìm thấy.
        -Vd:    s = "Hello World"
                print(s.find("World"))  # Output: 6
    startswith(chuỗi con): Kiểm tra chuỗi có bắt đầu bằng chuỗi con không.
    endswith(chuỗi con): Kiểm tra chuỗi có kết thúc bằng chuỗi con không.
        -Vd:    s = "Hello World"
                print(s.startswith("Hello"))  # Output: True
                print(s.endswith("World"))    # Output: True
    isdigit(): Kiểm tra chuỗi chỉ chứa các ký tự số.
    isalpha(): Kiểm tra chuỗi chỉ chứa các ký tự chữ.
    isalnum(): Kiểm tra chuỗi chỉ chứa các ký tự chữ và số.
    format(): Sử dụng để chèn các giá trị vào chuỗi bằng cách sử dụng dấu ngoặc nhọn {}.
        -Vd:    name = "Thuận"
                age = 30
                sentence = "Tên tôi là {}, năm nay tôi {} tuổi.".format(name, age)
                print(sentence)  # Output: "Tên tôi là Thuận, năm nay tôi 30 tuổi."
'''