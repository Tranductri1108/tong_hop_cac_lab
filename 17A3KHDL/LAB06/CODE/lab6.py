import tkinter as tk
from tkinter import messagebox
import sqlite3

# Tạo hoặc kết nối đến cơ sở dữ liệu
conn = sqlite3.connect("LAB06/DATA/products.db")
cursor = conn.cursor()

# Tạo bảng nếu chưa tồn tại
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")
conn.commit()

# Hàm thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    quantity = entry_quantity.get()
    if name and price and quantity:
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, float(price), int(quantity)))
        conn.commit()
        update_listbox()
        clear_entries()
    else:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin.")

# Hàm cập nhật danh sách sản phẩm
def update_listbox():
    listbox_products.delete(0, tk.END)
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        listbox_products.insert(tk.END, f"{row[0]} - {row[1]} - ${row[2]} - SL: {row[3]}")

# Hàm xóa sản phẩm
def delete_product():
    selected = listbox_products.curselection()
    if selected:
        product_id = int(listbox_products.get(selected).split(" - ")[0])
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        update_listbox()
    else:
        messagebox.showwarning("Lỗi", "Vui lòng chọn sản phẩm để xóa.")

# Hàm xóa nội dung trong các ô nhập liệu
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# Giao diện chính
root = tk.Tk()
root.title("Quản lý sản phẩm")

# Các widget
tk.Label(root, text="Tên sản phẩm").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Giá").grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

tk.Label(root, text="Số lượng").grid(row=2, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=2, column=1)

btn_add = tk.Button(root, text="Thêm sản phẩm", command=add_product)
btn_add.grid(row=3, column=0, columnspan=2)

listbox_products = tk.Listbox(root, width=50)
listbox_products.grid(row=4, column=0, columnspan=2)

btn_delete = tk.Button(root, text="Xóa sản phẩm", command=delete_product)
btn_delete.grid(row=5, column=0, columnspan=2)

# Khởi tạo danh sách sản phẩm
update_listbox()

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát
conn.close()
