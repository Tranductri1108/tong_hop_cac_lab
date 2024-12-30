import pandas as pd

# Bước 1: Đọc file stocks1.csv và stocks2.csv vào DataFrame stocks1 và stocks2
stocks1 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks1.csv')
stocks2 = pd.read_csv('D:\DHKL17A3\LAB3\DATA\stocks2.csv')

# Bước 2: Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Bước 3: Đọc file companies.csv vào DataFrame companies
companies = pd.read_csv('D:\DHKL17A3\LAB3\DATA\companies.csv')

# Hiển thị 5 dòng đầu tiên của companies
print("5 dòng đầu tiên của DataFrame companies:")  # (In tiêu đề)
print(companies.head())  # (Hiển thị 5 dòng đầu tiên của DataFrame companies)

# Bước 4: Xử lý lỗi có thể xảy ra khi tên cột không đúng (loại bỏ khoảng trắng thừa)
stocks.columns = stocks.columns.str.strip()
companies.columns = companies.columns.str.strip()

# Bước 5: Kết hợp stocks và companies dựa trên cột 'symbol' và 'name' (nếu cần thiết)
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name')

# Bước 6: Tính giá đóng cửa (close) trung bình cho mỗi công ty
average_close = merged_data.groupby('name')['close'].mean()

# Bước 7: Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình cho mỗi công ty:")
print(average_close.head())
