import sqlite3

# Kết nối đến cơ sở dữ liệu (tệp sẽ được tạo nếu chưa tồn tại)
conn = sqlite3.connect('phong.db')
cursor = conn.cursor()

# Tạo bảng PHONG
cursor.execute("""
CREATE TABLE IF NOT EXISTS PHONG (
    Ma_phong VARCHAR(10) PRIMARY KEY,
    Ten_phong VARCHAR(50),
    So_nguoi INT
);
""")

# Tạo bảng NHAN_VIEN
cursor.execute("""
CREATE TABLE IF NOT EXISTS NHAN_VIEN (
    Ma_nv VARCHAR(10) PRIMARY KEY,
    Id_phong VARCHAR(10),
    Ho_ten VARCHAR(100),
    Ngay_sinh DATE,
    GioiTinh CHAR(1),
    Dien_thoai VARCHAR(15),
    FOREIGN KEY (Id_phong) REFERENCES PHONG(Ma_phong)
);
""")

# Thêm dữ liệu vào bảng PHONG
cursor.executemany("""
INSERT OR IGNORE INTO PHONG (Ma_phong, Ten_phong, So_nguoi)
VALUES (?, ?, ?);
""", [
    ('A', 'Phòng A', 10),
    ('B', 'Phòng B', 15),
    ('C', 'Phòng C', 20)
])

# Thêm dữ liệu vào bảng NHAN_VIEN
cursor.executemany("""
INSERT OR IGNORE INTO NHAN_VIEN (Ma_nv, Id_phong, Ho_ten, Ngay_sinh, GioiTinh, Dien_thoai)
VALUES (?, ?, ?, ?, ?, ?);
""", [
    ('NV1', 'A', 'Nguyễn Văn A', '1990-01-01', 'M', '0123456789'),
    ('NV2', 'B', 'Trần Thị B', '1991-02-02', 'F', '0987654321'),
    ('NV3', 'C', 'Lê Văn C', '1992-03-03', 'M', '0777777777')
])

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()
import sqlite3

# Kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('phong.db')
cursor = conn.cursor()

# Hàm hiển thị dữ liệu từ bảng PHONG
def display_phong():
    print("Bảng PHONG:")
    cursor.execute("SELECT * FROM PHONG")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Ma_phong: {row[0]}, Ten_phong: {row[1]}, So_nguoi: {row[2]}")
    print()

# Hàm hiển thị dữ liệu từ bảng NHAN_VIEN
def display_nhan_vien():
    print("Bảng NHAN_VIEN:")
    cursor.execute("SELECT * FROM NHAN_VIEN")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Ma_nv: {row[0]}, Id_phong: {row[1]}, Ho_ten: {row[2]}, Ngay_sinh: {row[3]}, GioiTinh: {row[4]}, Dien_thoai: {row[5]}")
    print()

# Gọi các hàm hiển thị
display_phong()
display_nhan_vien()

# Đóng kết nối
conn.close()
