import os
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


# key_setup
def load_or_create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
    with open("key.key", "rb") as f:
        return f.read()


key = load_or_create_key()
fer = Fernet(key)


# gui_app
def save_password():
    account = account_entry.get().strip()
    password = password_entry.get().strip()

    if not account or not password:
        messagebox.showwarning("Empty Field", "Please enter both account and password.")
        return

    encrypted = fer.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(account + " | " + encrypted + "\n")

    messagebox.showinfo("Saved", f"Password for '{account}' saved!")
    account_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def view_passwords():
    if not os.path.exists("passwords.txt"):
        messagebox.showinfo("Empty", "No saved passwords yet.")
        return

    with open("passwords.txt", "r") as f:
        entries = []
        for line in f:
            if "|" in line:
                user, enc = line.strip().split("|")
                try:
                    dec = fer.decrypt(enc.strip().encode()).decode()
                    entries.append(f"{user.strip()} | {dec}")
                except:
                    entries.append(f"{user.strip()} | [decryption error]")
        messagebox.showinfo("Saved Passwords", "\n".join(entries))


# main_window
root = tk.Tk()
root.title("🔐 Simple Password Manager")
root.geometry("350x250")
root.resizable(False, False)

tk.Label(root, text="Account Name").pack(pady=(20, 5))
account_entry = tk.Entry(root, width=30)
account_entry.pack()

tk.Label(root, text="Password").pack(pady=(10, 5))
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

tk.Button(root, text="Save Password", command=save_password, width=25).pack(
    pady=(15, 5)
)
tk.Button(root, text="View Passwords", command=view_passwords, width=25).pack()
tk.Button(root, text="Exit", command=root.quit, width=25).pack(pady=(5, 5))

root.mainloop()
