import math

def do_dai_AB(xA, yA, xB, yB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2)

xA = float(input("Nhập tọa độ x của điểm A: "))
yA = float(input("Nhập tọa độ y của điểm A: "))
xB = float(input("Nhập tọa độ x của điểm B: "))
yB = float(input("Nhập tọa độ y của điểm B: "))

do_dai = do_dai_AB(xA, yA, xB, yB)

print("Độ dài đoạn AB là:", do_dai)
