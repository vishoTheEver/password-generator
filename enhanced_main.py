import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        nr_letters = int(letters_entry.get())
        nr_symbols = int(symbols_entry.get())
        nr_numbers = int(numbers_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return

    letters = string.ascii_letters
    numbers = string.digits
    symbols = '!#$%&()*+'

    selected_letters = [random.choice(letters) for _ in range(nr_letters)]
    selected_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    selected_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_characters = selected_letters + selected_symbols + selected_numbers
    random.shuffle(password_characters)
    password = ''.join(password_characters)

    password_output.delete(1.0, tk.END)
    password_output.insert(tk.END, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_output.get(1.0, tk.END).strip()  # Remove newline at the end
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()  # This is required to finalize the clipboard update
    messagebox.showinfo("Info", "Password copied to clipboard!")

app = tk.Tk()
app.title("Password Generator")

# Labels
tk.Label(app, text="How many letters?").grid(row=0, column=0)
tk.Label(app, text="How many symbols?").grid(row=1, column=0)
tk.Label(app, text="How many numbers?").grid(row=2, column=0)

# Entry fields
letters_entry = tk.Entry(app)
letters_entry.grid(row=0, column=1, padx=10, pady=10)

symbols_entry = tk.Entry(app)
symbols_entry.grid(row=1, column=1, padx=10, pady=10)

numbers_entry = tk.Entry(app)
numbers_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to generate the password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Output area for the password
password_output = tk.Text(app, height=2, width=30)
password_output.grid(row=4, column=0, columnspan=2, pady=20)

# Button to copy the password
copy_button = tk.Button(app, text="Copy Password", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
