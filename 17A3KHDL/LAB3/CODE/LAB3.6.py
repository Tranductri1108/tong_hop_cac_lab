import pandas as pd
stocks1 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks1.csv')  
stocks2 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks2.csv') 


stocks = pd.concat([stocks1, stocks2], ignore_index=True) 

#Tạo Pivot Table với 'date' làm chỉ mục, 'symbol' làm cột, và giá trị trung bình của 'close' làm giá trị
pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')

# Thêm một cột tính tổng 'volume' giao dịch cho mỗi mã chứng khoán (symbol)
pivot_table['total_volume'] = stocks.groupby('symbol')['volume'].sum()

#Sắp xếp Pivot Table theo tổng volume giao dịch, từ cao xuống thấp
pivot_table_sorted = pivot_table.sort_values(by='total_volume', ascending=False)

#Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
print(pivot_table_sorted.head())  