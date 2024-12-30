import sqlite3

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('your_database.db')

# Tạo một đối tượng cursor để thực hiện các câu lệnh SQL
cursor = conn.cursor()

# Liệt kê các bảng trong cơ sở dữ liệu
cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type='table';
""")

# Lấy kết quả
tables = cursor.fetchall()

# In tên các bảng
print("Các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(f"- {table[0]}")

# Đóng kết nối
conn.close()
