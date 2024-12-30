import pandas as pd

# Đọc file stocks1.csv vào DataFrame stocks1
stocks1 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks1.csv')

#1: Kiểm tra dữ liệu Null
print("Kiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())

#2: Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
if stocks1['high'].isnull().any():
    high_mean = stocks1['high'].mean()
    stocks1['high'].fillna(high_mean, inplace=True)
    print(f"\nĐã thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình: {high_mean:.2f}")

#3: Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
if stocks1['low'].isnull().any():
    low_mean = stocks1['low'].mean()
    stocks1['low'].fillna(low_mean, inplace=True)
    print(f"Đã thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình: {low_mean:.2f}")

#4: Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
stocks1.info()

# Kiểm tra lại xem còn dữ liệu Null không
print("\nKiểm tra lại dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())
