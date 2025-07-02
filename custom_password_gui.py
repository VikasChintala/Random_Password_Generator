import customtkinter as ctk
import random
import string

# App settings
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")


def generate_password():
    try:
        length = int(length_entry.get())
        chars = string.ascii_lowercase
        if uppercase_var.get():
            chars += string.ascii_uppercase
        if digits_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        output_entry.delete(0, ctk.END)
        output_entry.insert(0, password)
    except ValueError:
        output_entry.delete(0, ctk.END)
        output_entry.insert(0, "Enter a valid number!")

# Create the main app window
app = ctk.CTk()
app.title("Custom Password Generator")
app.geometry("400x400")

# Title
title_label = ctk.CTkLabel(app, text="🔐 Password Generator", font=("Arial", 20))
title_label.pack(pady=10)

# Length input
length_label = ctk.CTkLabel(app, text="Password Length:")
length_label.pack()
length_entry = ctk.CTkEntry(app, width=200)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Checkboxes
uppercase_var = ctk.BooleanVar()
digits_var = ctk.BooleanVar()
symbols_var = ctk.BooleanVar()

uppercase_checkbox = ctk.CTkCheckBox(app, text="Include Uppercase", variable=uppercase_var)
digits_checkbox = ctk.CTkCheckBox(app, text="Include Numbers", variable=digits_var)
symbols_checkbox = ctk.CTkCheckBox(app, text="Include Symbols", variable=symbols_var)

uppercase_checkbox.pack()
digits_checkbox.pack()
symbols_checkbox.pack()

# Generate button
generate_button = ctk.CTkButton(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=15)

# Output
output_label = ctk.CTkLabel(app, text="Generated Password:")
output_label.pack()
output_entry = ctk.CTkEntry(app, width=250)
output_entry.pack(pady=5)

# Run the app
app.mainloop()
