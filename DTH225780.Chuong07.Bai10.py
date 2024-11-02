import json
import os

class SinhVien:
    def __init__(self, ma_sv, ten_sv, nam_sinh):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.nam_sinh = nam_sinh

    def to_dict(self):
        return {"ma_sv": self.ma_sv, "ten_sv": self.ten_sv, "nam_sinh": self.nam_sinh}

class Lop:
    def __init__(self, ma_lop, ten_lop):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop
        self.sinh_vien_list = []

    def to_dict(self):
        return {
            "ma_lop": self.ma_lop,
            "ten_lop": self.ten_lop,
            "sinh_vien_list": [sv.to_dict() for sv in self.sinh_vien_list]
        }

class QuanLySinhVien:
    def __init__(self, file_path="sinhvien.json"):
        self.file_path = file_path
        self.lop_list = []
        self.doc_du_lieu()

    def them_lop(self, ma_lop, ten_lop):
        lop = Lop(ma_lop, ten_lop)
        self.lop_list.append(lop)

    def them_sinh_vien(self, ma_sv, ten_sv, nam_sinh, ma_lop):
        for lop in self.lop_list:
            if lop.ma_lop == ma_lop:
                sinh_vien = SinhVien(ma_sv, ten_sv, nam_sinh)
                lop.sinh_vien_list.append(sinh_vien)
                return
        print("Không tìm thấy lớp.")

    def sua_sinh_vien(self, ma_sv, ten_sv=None, nam_sinh=None):
        for lop in self.lop_list:
            for sv in lop.sinh_vien_list:
                if sv.ma_sv == ma_sv:
                    if ten_sv: sv.ten_sv = ten_sv
                    if nam_sinh: sv.nam_sinh = nam_sinh
                    return
        print("Không tìm thấy sinh viên.")

    def xoa_sinh_vien(self, ma_sv):
        for lop in self.lop_list:
            lop.sinh_vien_list = [sv for sv in lop.sinh_vien_list if sv.ma_sv != ma_sv]

    def tim_kiem(self, ten_sv):
        for lop in self.lop_list:
            for sv in lop.sinh_vien_list:
                if ten_sv.lower() in sv.ten_sv.lower():
                    print(sv.to_dict())

    def sap_xep(self):
        for lop in self.lop_list:
            lop.sinh_vien_list.sort(key=lambda sv: sv.ten_sv)

    def luu_du_lieu(self):
        with open(self.file_path, "w") as f:
            json.dump([lop.to_dict() for lop in self.lop_list], f, indent=4)

    def doc_du_lieu(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                for lop_data in data:
                    lop = Lop(lop_data["ma_lop"], lop_data["ten_lop"])
                    for sv_data in lop_data["sinh_vien_list"]:
                        sinh_vien = SinhVien(sv_data["ma_sv"], sv_data["ten_sv"], sv_data["nam_sinh"])
                        lop.sinh_vien_list.append(sinh_vien)
                    self.lop_list.append(lop)

qlsv = QuanLySinhVien()

qlsv.them_lop("L01", "Công Nghệ Thông Tin")
qlsv.them_sinh_vien("SV01", "Nguyễn Văn A", 2000, "L01")
qlsv.them_sinh_vien("SV02", "Trần Thị B", 2001, "L01")
qlsv.luu_du_lieu()

qlsv.tim_kiem("Nguyễn")
qlsv.sap_xep()
qlsv.luu_du_lieu()
