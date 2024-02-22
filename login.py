import tkinter as tk
from tkinter import messagebox
from test1 import CustomFrame1

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Login")
        label.pack(pady=10, padx=10)
        
        username_label = tk.Label(self, text="Username")
        username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        password_label = tk.Label(self, text="Password")
        password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self, text="Login", command=lambda: self.login(controller))
        login_button.pack()

    def login(self, controller):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Here you would typically check the credentials against a database or other storage
        if username == "a" and password == "z":
            messagebox.showinfo("Login Successful", "Welcome!")
            controller.show_frame(CustomFrame1)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

