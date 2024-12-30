import sqlite3

# Tạo kết sở dữ liệu
conn = sqlite3.connect('example.db')

# Lấy phiên bản của SQLite
version = sqlite3.version

# In ra phiên bản
print("Version của SQLite:", version)

# Tạo một bảng mới
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

# Đóng kết nối
conn.close