import tkinter as tk
from tkinter import messagebox
from acount_creation import Acount_creation
from room import Room
from User import User
from database import Database

class Login(tk.Frame):
    def __init__(self, parent, controller):
        # Convert RGB values to hexadecimal color code
        bg_color = "#1E1E1E"  # This is the hexadecimal equivalent of RGB(30,  30,  30)
        tk.Frame.__init__(self, parent, bg="#313338")  # Set a background color
        self.configure(padx=20, pady=20)  # Increase padding around the frame

        # Similarly, set the background color for the label using a hexadecimal color code
        label = tk.Label(self, text="Login", font=("Helvetica",   20), fg="#f2f3f5", bg="#313338")  # Increase font size and set background color
        label.pack(pady=10)
        
        # The rest of your code remains the same
        username_label = tk.Label(self, text="Pseudo", font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")  # Increase font size and set background color
        username_label.pack()

        self.username_entry = tk.Entry(self, font=("Helvetica",  14))  # Increase font size
        self.username_entry.pack()

        password_label = tk.Label(self, text="Password", font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")  # Increase font size and set background color
        password_label.pack()

        self.password_entry = tk.Entry(self, show="*", font=("Helvetica",  14))  # Increase font size
        self.password_entry.pack()

        login_button = tk.Button(self, text="Login", command=lambda: self.login(controller), font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")  # Increase font size, change background and text color
        login_button.pack(pady=10)

        new_acount_button = tk.Button(self, text="Inscription", command=lambda: controller.show_frame(Acount_creation), font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")  # Increase font size, change background and text color
        new_acount_button.pack(pady=10)

    def login(self, controller):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Here you would typically check the credentials against a database or other storage
        test_user = User (Database(host="localhost", user="root", password="2879", database="mydiscord"))
        user_info = test_user.read_user_pseudo (username)
        if password == user_info [0][4] :
            messagebox.showinfo("Login Successful", "Welcome!")
            controller.show_frame(Room)

