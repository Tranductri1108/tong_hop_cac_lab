import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('example.db')

# Tạo cursor
cursor = conn.cursor()

# Tạo bảng
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
""")

# Chèn dữ liệu vào bảng
cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Jane Doe', 25)")

# Commit changes
conn.commit()

# Truy vấn dữ liệu
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# In ra kết quả
for row in rows:
    print(row)

# Đóng kết nối
conn.close()