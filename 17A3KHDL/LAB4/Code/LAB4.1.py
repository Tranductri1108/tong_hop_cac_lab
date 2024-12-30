import sqlite3

# Kết nối tới CSDL SQLite hoặc tạo mới nếu chưa tồn tại
ket_noi = sqlite3.connect("D:\DHKL17A3\THUCHANH\LAB4\Data\product.db")
truy_van = ket_noi.cursor()

# Tạo bảng sản phẩm
truy_van.execute('''
CREATE TABLE IF NOT EXISTS sanpham (
    id INTEGER PRIMARY KEY,
    ten TEXT NOT NULL,
    gia REAL NOT NULL,
    so_luong INTEGER NOT NULL
)
''')

# Hàm hiển thị danh sách sản phẩm
def hien_thi_san_pham():
    truy_van.execute("SELECT * FROM sanpham")
    danh_sach = truy_van.fetchall()
    if danh_sach:
        print(f"{'ID':<5}{'Tên':<20}{'Giá':<10}{'Số lượng':<10}")
        for sp in danh_sach:
            print(f"{sp[0]:<5}{sp[1]:<20}{sp[2]:<10}{sp[3]:<10}")
    else:
        print("Không có sản phẩm nào.")

# Hàm thêm sản phẩm mới
def them_san_pham():
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    so_luong = int(input("Nhập số lượng sản phẩm: "))
    truy_van.execute("INSERT INTO sanpham (ten, gia, so_luong) VALUES (?, ?, ?)", (ten, gia, so_luong))
    ket_noi.commit()
    print("Đã thêm sản phẩm thành công.")

# Hàm tìm kiếm sản phẩm theo tên
def tim_kiem_san_pham():
    ten = input("Nhập tên sản phẩm để tìm kiếm: ")
    truy_van.execute("SELECT * FROM sanpham WHERE ten LIKE ?", ('%' + ten + '%',))
    ket_qua = truy_van.fetchall()
    if ket_qua:
        print(f"{'ID':<5}{'Tên':<20}{'Giá':<10}{'Số lượng':<10}")
        for sp in ket_qua:
            print(f"{sp[0]:<5}{sp[1]:<20}{sp[2]:<10}{sp[3]:<10}")
    else:
        print("Không tìm thấy sản phẩm nào.")

# Hàm cập nhật thông tin sản phẩm
def cap_nhat_san_pham():
    id_sp = int(input("Nhập ID sản phẩm cần cập nhật: "))
    truy_van.execute("SELECT * FROM sanpham WHERE id = ?", (id_sp,))
    sp = truy_van.fetchone()
    if sp:
        print(f"Tên hiện tại: {sp[1]}, Giá hiện tại: {sp[2]}, Số lượng hiện tại: {sp[3]}")
        ten = input("Nhập tên mới (bấm Enter để giữ nguyên): ") or sp[1]
        gia = input("Nhập giá mới (bấm Enter để giữ nguyên): ")
        gia = float(gia) if gia else sp[2]
        so_luong = input("Nhập số lượng mới (bấm Enter để giữ nguyên): ")
        so_luong = int(so_luong) if so_luong else sp[3]
        truy_van.execute("UPDATE sanpham SET ten = ?, gia = ?, so_luong = ? WHERE id = ?", (ten, gia, so_luong, id_sp))
        ket_noi.commit()
        print("Cập nhật sản phẩm thành công.")
    else:
        print("Không tìm thấy sản phẩm.")

# Hàm xóa sản phẩm
def xoa_san_pham():
    id_sp = int(input("Nhập ID sản phẩm cần xóa: "))
    truy_van.execute("DELETE FROM sanpham WHERE id = ?", (id_sp,))
    ket_noi.commit()
    print("Đã xóa sản phẩm thành công.")

# Menu chính
def menu_chinh():
    while True:
        print("\nHệ thống quản lý sản phẩm")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            hien_thi_san_pham()
        elif lua_chon == '2':
            them_san_pham()
        elif lua_chon == '3':
            tim_kiem_san_pham()
        elif lua_chon == '4':
            cap_nhat_san_pham()
        elif lua_chon == '5':
            xoa_san_pham()
        elif lua_chon == '6':
            print("Đã thoát chương trình ")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    menu_chinh()

# Đóng kết nối khi chương trình kết thúc
ket_noi.close()
