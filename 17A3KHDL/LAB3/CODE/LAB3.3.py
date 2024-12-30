import pandas as pd

#1: Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks2.csv')

# Đọc lại stocks1 từ LAB 3.1 (giả sử đã được xử lý Null trong LAB 3.2)
stocks1 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks1.csv')

#2: Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

#3: Tính giá trung bình (open, high, low, close) cho mỗi ngày
average_prices = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

#4: Hiển thị 5 dòng đầu tiên của kết quả
print("Giá trung bình (open, high, low, close) cho mỗi ngày:")
print(average_prices.head())
