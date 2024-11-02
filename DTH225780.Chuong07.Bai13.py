import xml.etree.ElementTree as ET
from collections import defaultdict

def hien_thi_danh_sach_nhom(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("Danh sách Nhóm thiết bị:")
    for nhom in root.findall('nhom'):
        ma = nhom.find('ma').text
        ten = nhom.find('ten').text
        print(f"Mã nhóm: {ma}, Tên nhóm: {ten}")

def hien_thi_danh_sach_thiet_bi(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("Danh sách Thiết bị:")
    for thietbi in root.findall('thietbi'):
        manhom = thietbi.get('manhom')
        ma = thietbi.find('ma').text
        ten = thietbi.find('ten').text
        print(f"Mã nhóm: {manhom}, Mã thiết bị: {ma}, Tên thiết bị: {ten}")

def loc_thiet_bi_theo_nhom(file_path, manhom_filter):
    tree = ET.parse(file_path)
    root = tree.getroot()
    print(f"Thiết bị thuộc nhóm {manhom_filter}:")
    for thietbi in root.findall('thietbi'):
        if thietbi.get('manhom') == manhom_filter:
            ma = thietbi.find('ma').text
            ten = thietbi.find('ten').text
            print(f"Mã thiết bị: {ma}, Tên thiết bị: {ten}")

def nhom_nhieu_thiet_bi_nhat(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    thietbi_count = defaultdict(int)
    for thietbi in root.findall('thietbi'):
        manhom = thietbi.get('manhom')
        thietbi_count[manhom] += 1
    max_nhom = max(thietbi_count, key=thietbi_count.get)
    print(f"Nhóm có số lượng thiết bị nhiều nhất là nhóm '{max_nhom}' với {thietbi_count[max_nhom]} thiết bị.")

file_nhom = 'nhomthietbi.xml'
file_thietbi = 'ThietBi.xml'

hien_thi_danh_sach_nhom(file_nhom)
print("\n")
hien_thi_danh_sach_thiet_bi(file_thietbi)
print("\n")
loc_thiet_bi_theo_nhom(file_thietbi, "n1")
print("\n")
nhom_nhieu_thiet_bi_nhat(file_thietbi)
