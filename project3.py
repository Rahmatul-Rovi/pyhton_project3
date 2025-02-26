import tkinter as tk
from tkinter import messagebox

# Sample product list stored in memory
products = {
    "Apple": 50,
    "Banana": 20,
    "Orange": 30,
    "Milk": 80,
    "Bread": 40,
    "Eggs": 100,
    "Rice": 60,
    "Sugar": 45
}

cart = {}

def add_to_cart():
    product = product_var.get()
    quantity = quantity_var.get()
    
    if product and quantity.isdigit():
        quantity = int(quantity)
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        
        update_cart()
    else:
        messagebox.showerror("Error", "Please select a valid product and enter a valid quantity.")

def update_cart():
    cart_list.delete(0, tk.END)
    total_price = 0
    
    for item, qty in cart.items():
        price = products[item] * qty
        total_price += price
        cart_list.insert(tk.END, f"{item} x {qty} = {price} Rs")
    
    total_label.config(text=f"Total: {total_price} Rs")

def generate_bill():
    if not cart:
        messagebox.showwarning("Warning", "Cart is empty!")
        return
    
    bill_text = "\nBILL RECEIPT\n-------------------\n"
    total_price = 0
    for item, qty in cart.items():
        price = products[item] * qty
        total_price += price
        bill_text += f"{item} x {qty} = {price} Rs\n"
    
    bill_text += f"-------------------\nTotal: {total_price} Rs"
    messagebox.showinfo("Bill Generated", bill_text)

def clear_cart():
    cart.clear()
    update_cart()

def remove_item():
    selected = cart_list.curselection()
    if selected:
        item = cart_list.get(selected[0]).split(" x ")[0]
        del cart[item]
        update_cart()
    else:
        messagebox.showwarning("Warning", "Select an item to remove.")

def apply_discount():
    discount = discount_var.get()
    if discount.isdigit():
        discount = int(discount)
        total_price = sum(products[item] * qty for item, qty in cart.items())
        discounted_price = total_price - (total_price * discount / 100)
        total_label.config(text=f"Total after {discount}% discount: {discounted_price} Rs")
    else:
        messagebox.showerror("Error", "Enter a valid discount percentage.")

# GUI Setup
root = tk.Tk()
root.title("Billing System")
root.geometry("400x600")

tk.Label(root, text="Select Product:").pack()
product_var = tk.StringVar()
product_menu = tk.OptionMenu(root, product_var, *products.keys())
product_menu.pack()

tk.Label(root, text="Enter Quantity:").pack()
quantity_var = tk.StringVar()
tk.Entry(root, textvariable=quantity_var).pack()

tk.Button(root, text="Add to Cart", command=add_to_cart).pack()

tk.Label(root, text="Cart:").pack()
cart_list = tk.Listbox(root)
cart_list.pack()

total_label = tk.Label(root, text="Total: 0 Rs", font=("Arial", 12, "bold"))
total_label.pack()

tk.Label(root, text="Enter Discount (%):").pack()
discount_var = tk.StringVar()
tk.Entry(root, textvariable=discount_var).pack()
tk.Button(root, text="Apply Discount", command=apply_discount).pack()

tk.Button(root, text="Remove Item", command=remove_item).pack()
tk.Button(root, text="Generate Bill", command=generate_bill).pack()
tk.Button(root, text="Clear Cart", command=clear_cart).pack()

tk.Button(root, text="Exit", command=root.quit).pack()

root.mainloop()
