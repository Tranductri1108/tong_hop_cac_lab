import sqlite3
# Tạo kết nối tới cơ sở dữ liệu SQLite. H
conn = sqlite3.connect('TestDB.db')
# Tạo một con trỏ đến cơ sở dữ liệu
cur = conn.cursor()
# Tạo bảng:
cur.execute('''CREATE TABLE employees
 (first_name text, last_name text)''')