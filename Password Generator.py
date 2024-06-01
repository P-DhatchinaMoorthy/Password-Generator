import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

def generate_password():
    try:    
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6 characters")
            return

        selected_types = []
        if letters.get():
            selected_types.append(string.ascii_letters)
        if numbers.get():
            selected_types.append(string.digits)
        if punctuation.get():
            selected_types.append(string.punctuation)

        if not selected_types:
            messagebox.showerror("Error", "Please select at least one character type")
            return

        all_characters = ''.join(selected_types)

        password = ''.join(random.choices(all_characters,k=length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror('Error','Enter a valid number')

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def clipboard_copy():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")
root.configure(background='#66c2ff')

length_label = tk.Label(root, text="Password Length:", background='#66c2ff', foreground='black')
length_label.place(x=20,y=20)

length_entry = tk.Entry(root)
length_entry.place(x=140,y=20)

letters = tk.BooleanVar()
letters_checkbox = ttk.Checkbutton(root, text="Letters", variable=letters)
letters_checkbox.place(x=20,y=60)

numbers= tk.BooleanVar()
numbers_checkbox = ttk.Checkbutton(root, text="Numbers", variable=numbers)
numbers_checkbox.place(x=78,y=60)

punctuation = tk.BooleanVar()
punctuation_checkbox = ttk.Checkbutton(root, text="Punctuation", variable=punctuation)
punctuation_checkbox.place(x=150,y=60)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, background='#66c2ff', foreground='black')
generate_button.place(x=20,y=100)

password_entry = tk.Entry(root, show="*", background='white', foreground='black')
password_entry.place(x=150,y=100)

show_password_var = tk.BooleanVar()
show_password_checkbox = ttk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.place(x=150,y=130)

clipboard_var = tk.BooleanVar()
clipboard_checkbox = ttk.Checkbutton(root, text="Copy Password", variable=clipboard_var, command=clipboard_copy)
clipboard_checkbox.place(x=150,y=155)

root.mainloop()