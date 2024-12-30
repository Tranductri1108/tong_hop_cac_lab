import numpy as np

# Bước 1: Đọc dữ liệu từ hai tệp vào list
with open('D:\DHKL17A3\LAB2\DATA\efficiency.txt', 'r') as eff_file:
    efficiency = [float(line.strip()) for line in eff_file.readlines()]

with open('D:\DHKL17A3\LAB2\DATA\shifts.txt', 'r') as shifts_file:
    shifts = [line.strip() for line in shifts_file.readlines()]

# Bước 2: Tạo numpy array từ list shifts và kiểm tra kiểu dữ liệu
np_shifts = np.array(shifts)
print(f"Kiểu dữ liệu của np_shifts: {np_shifts.dtype}")

# Bước 3: Tạo numpy array từ list efficiency và kiểm tra kiểu dữ liệu
np_efficiency = np.array(efficiency)
print(f"Kiểu dữ liệu của np_efficiency: {np_efficiency.dtype}")

# Bước 4: Tính hiệu suất trung bình của nhân viên làm việc ca 'Morning'
morning_mask = np_shifts == 'Morning'
morning_efficiency = np_efficiency[morning_mask]
average_morning_efficiency = np.mean(morning_efficiency)
print(f"Hiệu suất trung bình của ca 'Morning': {average_morning_efficiency:.2f}")

# Bước 5: Tính hiệu suất trung bình của nhân viên làm việc ca khác ('Afternoon' và 'Night')
non_morning_mask = np_shifts != 'Morning'
non_morning_efficiency = np_efficiency[non_morning_mask]
average_non_morning_efficiency = np.mean(non_morning_efficiency)
print(f"Hiệu suất trung bình của các ca khác: {average_non_morning_efficiency:.2f}")

# Bước 6: Tạo mảng dữ liệu có cấu trúc (Structured Array)
dtype = [('shift', 'U10'), ('efficiency', 'float')]
workers = np.array(list(zip(np_shifts, np_efficiency)), dtype=dtype)
print(f"Mảng workers:\n{workers}")

# Bước 7: Sắp xếp mảng workers theo efficiency và xác định ca làm việc có hiệu suất cao nhất, thấp nhất
sorted_workers = np.sort(workers, order='efficiency')
highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']

print(f"Ca làm việc có hiệu suất cao nhất: {highest_efficiency_shift}")
print(f"Ca làm việc có hiệu suất thấp nhất: {lowest_efficiency_shift}")
