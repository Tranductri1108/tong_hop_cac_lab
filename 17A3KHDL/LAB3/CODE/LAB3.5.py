import pandas as pd

stocks1 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks1.csv')  
stocks2 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks2.csv')  

stocks = pd.concat([stocks1, stocks2], ignore_index=True)

#Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột 'date' và 'symbol' làm chỉ mục
stocks.set_index(['date', 'symbol'], inplace=True)

#Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, mỗi mã chứng khoán
grouped_data = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',      
    'high': 'mean',       
    'low': 'mean',        
    'close': 'mean',      
    'volume': 'mean'    
}).reset_index()

# Bước 5: Sắp xếp dữ liệu theo ngày và mã chứng khoán
sorted_data = grouped_data.sort_values(by=['date', 'symbol'])  

# Bước 6: Hiển thị kết quả cho 5 ngày đầu tiên
print(sorted_data.head()) 
