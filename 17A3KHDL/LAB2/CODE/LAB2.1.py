import numpy as np

# Bước 1: Tạo Dữ Liệu Mô Phỏng Nhiệt Độ
# Tạo mảng nhiệt độ (30 ngày), làm tròn đến 2 chữ số
np.random.seed(0)
temperatures = np.round(np.random.uniform(15, 35, 30), 2)

# Tính nhiệt độ trung bình trong tháng
average_temperature = np.mean(temperatures)
print(f"Nhiệt độ hàng ngày: {temperatures}")
print(f"Nhiệt độ trung bình trong tháng: {average_temperature:.2f}°C")

# Bước 2: Phân Tích Xu Hướng Nhiệt Độ
# Tìm ngày có nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
day_max_temp = np.argmax(temperatures) + 1 
day_min_temp = np.argmin(temperatures) + 1
print(f"Nhiệt độ cao nhất: {max_temp}°C vào ngày thứ {day_max_temp}")
print(f"Nhiệt độ thấp nhất: {min_temp}°C vào ngày thứ {day_min_temp}")

# Chênh lệch nhiệt độ giữa các ngày
temp_diff = np.abs(np.diff(temperatures))
max_diff = np.max(temp_diff)
day_max_diff = np.argmax(temp_diff) + 1  
print(f"Sự chênh lệch nhiệt độ cao nhất: {max_diff:.2f}°C giữa ngày {day_max_diff} và ngày {day_max_diff + 1}")

# Bước 3: Áp dụng Fancy Indexing
# Tất cả các ngày có nhiệt độ cao hơn 20°C
days_above_20 = np.where(temperatures > 20)[0] + 1
print(f"Các ngày có nhiệt độ cao hơn 20°C: {days_above_20}")

# Lấy nhiệt độ của ngày 5, 10, 15, 20, 25
specific_days = [5, 10, 15, 20, 25]
temps_specific_days = temperatures[np.array(specific_days) - 1]
print(f"Nhiệt độ các ngày 5, 10, 15, 20, 25: {temps_specific_days}")

# Nhiệt độ của các ngày có nhiệt độ trên trung bình
temps_above_avg = temperatures[temperatures > average_temperature]
print(f"Nhiệt độ các ngày trên mức trung bình: {temps_above_avg}")

# Nhiệt độ của các ngày chẵn và lẻ trong tháng
even_days_temps = temperatures[1::2]  
odd_days_temps = temperatures[0::2]  
print(f"Nhiệt độ các ngày chẵn: {even_days_temps}")
print(f"Nhiệt độ các ngày lẻ: {odd_days_temps}")
