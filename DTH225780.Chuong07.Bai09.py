import os

class QuanLySanPham:
    def __init__(self, file_path="sanpham.txt"):
        self.file_path = file_path
        self.san_pham_list = []
        self.doc_du_lieu()

    def them_san_pham(self, ma_sp, ten_sp, don_gia, ma_danh_muc):
        san_pham = {"ma_sp": ma_sp, "ten_sp": ten_sp, "don_gia": don_gia, "ma_danh_muc": ma_danh_muc}
        self.san_pham_list.append(san_pham)

    def sua_san_pham(self, ma_sp, ten_sp=None, don_gia=None):
        for sp in self.san_pham_list:
            if sp["ma_sp"] == ma_sp:
                if ten_sp: sp["ten_sp"] = ten_sp
                if don_gia: sp["don_gia"] = don_gia
                return

    def xoa_san_pham(self, ma_sp):
        self.san_pham_list = [sp for sp in self.san_pham_list if sp["ma_sp"] != ma_sp]

    def tim_kiem(self, ten_sp):
        for sp in self.san_pham_list:
            if ten_sp.lower() in sp["ten_sp"].lower():
                print(sp)

    def sap_xep(self):
        self.san_pham_list.sort(key=lambda sp: sp["ten_sp"])

    def luu_du_lieu(self):
        with open(self.file_path, "w") as f:
            for sp in self.san_pham_list:
                f.write(f"{sp['ma_sp']},{sp['ten_sp']},{sp['don_gia']},{sp['ma_danh_muc']}\n")

    def doc_du_lieu(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                for line in f:
                    ma_sp, ten_sp, don_gia, ma_danh_muc = line.strip().split(',')
                    san_pham = {"ma_sp": ma_sp, "ten_sp": ten_sp, "don_gia": float(don_gia), "ma_danh_muc": ma_danh_muc}
                    self.san_pham_list.append(san_pham)

qlsp = QuanLySanPham()

qlsp.them_san_pham("SP01", "iPhone 13", 25000000, "DM01")
qlsp.them_san_pham("SP02", "Samsung Galaxy S21", 20000000, "DM01")
qlsp.luu_du_lieu()

qlsp.tim_kiem("iPhone")
qlsp.sap_xep()
qlsp.luu_du_lieu()
