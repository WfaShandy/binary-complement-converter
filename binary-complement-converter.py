import tkinter as tk
from tkinter import ttk

def binary_to_complement1(binary):
    return ''.join('1' if bit == '0' else '0' for bit in binary)

def binary_to_complement2(binary):
    complement1 = binary_to_complement1(binary)
    complement2 = bin(int(complement1, 2) + 1)[2:]
    return complement2.zfill(len(binary))

def convert():
    input_value = entry.get().strip()
    mode = mode_var.get()
    
    if not set(input_value).issubset({'0', '1'}):
        result_label.config(text="Invalid Input! Use only 0 and 1.")
        return
    
    if mode == "Binary":
        comp1 = binary_to_complement1(input_value)
        comp2 = binary_to_complement2(input_value)
        result_label.config(text=f"Complement 1: {comp1}\nComplement 2: {comp2}")
    elif mode == "Complement 1":
        binary = binary_to_complement1(input_value)
        comp2 = binary_to_complement2(binary)
        result_label.config(text=f"Binary: {binary}\nComplement 2: {comp2}")
    elif mode == "Complement 2":
        comp1 = bin(int(input_value, 2) - 1)[2:].zfill(len(input_value))
        binary = binary_to_complement1(comp1)
        result_label.config(text=f"Binary: {binary}\nComplement 1: {comp1}")

# GUI Setup
root = tk.Tk()
root.title("Binary Complement Converter")
root.geometry("350x250")

tk.Label(root, text="Enter Binary:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack()

mode_var = tk.StringVar(value="Binary")
mode_menu = ttk.Combobox(root, textvariable=mode_var, values=["Binary", "Complement 1", "Complement 2"], state="readonly")
mode_menu.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack()

root.mainloop()
