def LuuFile(path, data):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(data + '\n')

def nhap_san_pham():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    don_gia = float(input("Nhập đơn giá: "))
    return f"{ma};{ten};{don_gia}VNĐ."

def luu_san_pham():
    data = nhap_san_pham()
    LuuFile("sanpham.txt", data)
    print("Sản phẩm đã được lưu vào file.")

def doc_danh_sach(path):
    with open(path, 'r', encoding='utf-8') as file:
        san_pham_list = [line.strip().split(';') for line in file]
    return san_pham_list

def xuat_danh_sach_san_pham():
    san_pham_list = doc_danh_sach("sanpham.txt")
    for sp in san_pham_list:
        print(f"Mã: {sp[0]}, Tên: {sp[1]}, Đơn giá: {sp[2]}")

def sap_xep_theo_don_gia_giam_dan():
    san_pham_list = doc_danh_sach("sanpham.txt")
    san_pham_list.sort(key=lambda x: float(x[2]), reverse=True)
    for sp in san_pham_list:
        print(f"Mã: {sp[0]}, Tên: {sp[1]}, Đơn giá: {sp[2]}")

def main():
    while True:
        print("\nQuản lý Sản phẩm")
        print("1. Nhập sản phẩm và lưu vào file")
        print("2. Xuất danh sách sản phẩm từ file")
        print("3. Sắp xếp sản phẩm theo đơn giá giảm dần")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            luu_san_pham()
        elif choice == '2':
            xuat_danh_sach_san_pham()
        elif choice == '3':
            sap_xep_theo_don_gia_giam_dan()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
