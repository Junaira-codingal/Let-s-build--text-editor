from tkinter import *
import tkinter as tk

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        interest = (principal * rate * time) / 100
        total_amount = principal + interest

        label_result.config(text=f"Interest: {interest:.2f}\nTotal: {total_amount:.2f}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.", fg="#D32F2F")

root = tk.Tk()
root.title("Interest Calculator")
root.configure(bg="#85c1e9")  # Fixed background color

label_principal = tk.Label(root, text="Enter Principal:", bg="#102958", fg="White", font=("Arial", 12))
label_principal.grid(row=0, column=0, padx=10, pady=5)

entry_principal = tk.Entry(root, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
entry_principal.grid(row=0, column=1, padx=10, pady=5)

label_rate = tk.Label(root, text="Enter Rate of Interest (%):", bg="#234583", fg="White", font=("Arial", 12))
label_rate.grid(row=1, column=0, padx=10, pady=5)

entry_rate = tk.Entry(root, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
entry_rate.grid(row=1, column=1, padx=10, pady=5)

label_time = tk.Label(root, text="Enter Time (Years):", bg="#2e559e", fg="White", font=("Arial", 12))
label_time.grid(row=2, column=0, padx=10, pady=5)

entry_time = tk.Entry(root, bg="#FFFFFF", fg="#000000", font=("Arial", 12))
entry_time.grid(row=2, column=1, padx=10, pady=5)

btn_calculate = tk.Button(root, text="Calculate", bg="#5778d1", fg="White", font=("Arial", 12), command=calculate_interest)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

