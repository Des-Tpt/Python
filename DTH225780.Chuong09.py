import numpy as np
from sklearn import linear_model

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

regr = linear_model.LinearRegression()
regr.fit(X, y)

print("Kết quả từ scikit-learn:")
print("Hệ số w_1 =", regr.coef_[0])
print("Hệ số chặn w_0 =", regr.intercept_)

yourHeight = int(input("Nhập chiều cao của bạn (cm): "))
yourWeight = regr.coef_[0] * yourHeight + regr.intercept_
print("Chiều cao của bạn là", yourHeight, "cm, dự đoán cân nặng là", yourWeight, "kg")
