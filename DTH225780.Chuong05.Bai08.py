import os

def lay_ten_bai_hat(duong_dan):
    return os.path.basename(duong_dan) # Lấy tên bài hát theo đường dẫn

def lay_ten_bai_hat_khong_duoi(duong_dan):
    ten_bai_hat = os.path.basename(duong_dan) # Lấy tên bài hát theo đường dẫn nhưng bỏ đuôi file
    return os.path.splitext(ten_bai_hat)[0] # os.path.splitext được dùng để tách phần tên và đuôi của file ra, [0] ở cuối dùng để loại bỏ phần đuôi, nếu không ten_bai_hat sẽ chứa 2 giá trị là name và đuôi.

duong_dan_file = input("Nhập đường dẫn file nhạc: ")

ten_bai_hat = lay_ten_bai_hat(duong_dan_file)
ten_bai_hat_khong_duoi = lay_ten_bai_hat_khong_duoi(duong_dan_file)

print("Tên bài hát:", ten_bai_hat)
print("Tên bài hát không đuôi:", ten_bai_hat_khong_duoi)
