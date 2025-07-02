import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_lowercase
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Window
root = tk.Tk()
root.title("Random Password Generator")

# Widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.grid(row=0, column=1)

use_upper = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=use_upper).grid(row=1, column=0, columnspan=2)
tk.Checkbutton(root, text="Include Digits", variable=use_digits).grid(row=2, column=0, columnspan=2)
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols).grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Generated Password:").grid(row=5, column=0)
result_entry = tk.Entry(root, width=30)
result_entry.grid(row=5, column=1)

root.mainloop()
