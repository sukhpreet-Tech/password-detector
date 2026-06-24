import tkinter as tk
import re

def type_effect(text, label, i=0):
    if i < len(text):
        label.config(text=label.cget("text") + text[i])
        label.after(20, type_effect, text, label, i+1)

def check_strength():
    password = entry.get()
    output.config(text="")  # clear
#
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*!]", password):
        strength += 1

    if strength == 5:
        msg = "ACCESS LEVEL: STRONG "
        color = "lime"
    elif strength >= 3:
        msg = "ACCESS LEVEL: MEDIUM "
        color = "orange"
    else:
        msg = "ACCESS LEVEL: WEAK "
        color = "red"

    output.config(fg=color)
    type_effect(msg, output)

# Window
root = tk.Tk()
root.title("Cyber Terminal")
root.geometry("500x300")
root.configure(bg="black")

# Title
title = tk.Label(root, text=">> CYBER SECURITY TERMINAL <<",
                 fg="lime", bg="black", font=("Consolas", 14))
title.pack(pady=10)

# Instruction
label = tk.Label(root, text="Enter Password:",
                 fg="lime", bg="black", font=("Consolas", 12))
label.pack()

# Entry
entry = tk.Entry(root, show="*", font=("Consolas", 12),
                 bg="black", fg="lime", insertbackground="lime")
entry.pack(pady=10)

# Button
btn = tk.Button(root, text="ANALYZE",
                command=check_strength,
                bg="black", fg="lime",
                activebackground="green",
                font=("Consolas", 10))
btn.pack(pady=10)

# Output
output = tk.Label(root, text="",
                  fg="lime", bg="black",
                  font=("Consolas", 12))
output.pack(pady=20)

root.mainloop()
