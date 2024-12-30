import numpy as np
import pandas as pd

# 1. Đọc dữ liệu từ file CSV
file_path = 'D:\DHKL17A3\LAB2\DATA\diem_hoc_phan.csv'

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv(file_path)
print("Dữ liệu từ file CSV:")
print(df)

# Lấy dữ liệu điểm số từ các cột HP1, HP2, HP3
diem_hp = df[['HP 1', 'HP 2', 'HP 3']].values 
print("\nMảng điểm học phần:")
print(diem_hp)

# 3. Quy đổi thang điểm 10 sang thang điểm chữ
def chuyen_diem_chu(diem):
    if 8.5 <= diem <= 10:
        return 'A'
    elif 8.0 <= diem < 8.5:
        return 'B+'
    elif 7.0 <= diem < 8.0:
        return 'B'
    elif 6.5 <= diem < 7.0:
        return 'C+'
    elif 5.5 <= diem < 6.5:
        return 'C'
    elif 5.0 <= diem < 5.5:
        return 'D+'
    elif 4.0 <= diem < 5.0:
        return 'D'
    else:
        return 'F'

diem_chu = np.vectorize(chuyen_diem_chu)(diem_hp)
print("\nMảng điểm chữ:")
print(diem_chu)

# 4. Phân tích điểm theo từng học phần
for i, hp in enumerate(['HP1', 'HP2', 'HP3']):
    print(f"\nPhân tích {hp}:")
    diem_hp_i = diem_hp[:, i]
    print(f"Tổng điểm: {np.sum(diem_hp_i):.2f}")
    print(f"Điểm trung bình: {np.mean(diem_hp_i):.2f}")
    print(f"Độ lệch chuẩn: {np.std(diem_hp_i):.2f}")

# 5. Thống kê số lượng sinh viên đạt các loại điểm chữ
print("\nThống kê số lượng sinh viên theo loại điểm:")
unique, counts = np.unique(diem_chu, return_counts=True)
for grade, count in zip(unique, counts):
    print(f"Loại điểm {grade}: {count} sinh viên")
