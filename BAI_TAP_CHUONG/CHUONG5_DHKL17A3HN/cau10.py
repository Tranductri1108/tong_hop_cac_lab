import sqlite3

# Kết nối đến CSDL
conn = sqlite3.connect('product.db')
cursor = conn.cursor()

# Hàm hiển thị danh sách sản phẩm
def display_products():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Id: {row[0]}, Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}")
    else:
        print("No products found.")

# Hàm thêm sản phẩm
def add_product(name, price, quantity):
    cursor.execute("INSERT INTO product (Name, Price, Quantity) VALUES (?, ?, ?)", (name, price, quantity))
    conn.commit()
    print(f"Product '{name}' added successfully.")

# Hàm tìm kiếm sản phẩm theo tên
def search_product_by_name(name):
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Id: {row[0]}, Name: {row[1]}, Price: {row[2]}, Quantity: {row[3]}")
    else:
        print("Product not found.")

# Hàm cập nhật đơn giá và số lượng của một sản phẩm theo id
def update_product_price_and_quantity(product_id, price, quantity):
    cursor.execute("UPDATE product SET Price = ?, Quantity = ? WHERE Id = ?", (price, quantity, product_id))
    conn.commit()
    print(f"Product updated successfully with Id: {product_id}")

# Hàm cập nhật đơn hàng theo id (giả lập)
def update_order(product_id):
    print(f"Order updated successfully for product with Id: {product_id}")

# Hàm chính
def main():
    while True:
        print("\nOptions:")
        print("1. Display Products")
        print("2. Add Product")
        print("3. Search Product by Name")
        print("4. Update Product Price and Quantity")
        print("5. Update Order")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(name, price, quantity)
        elif choice == '3':
            name = input("Enter product name to search: ")
            search_product_by_name(name)
        elif choice == '4':
            product_id = int(input("Enter product id to update: "))
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            update_product_price_and_quantity(product_id, price, quantity)
        elif choice == '5':
            product_id = int(input("Enter product id for order update: "))
            update_order(product_id)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Chạy chương trình chính
if __name__ == "__main__":
    main()
