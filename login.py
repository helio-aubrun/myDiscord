import tkinter as tk
from tkinter import messagebox
from acount_creation import Acount_creation
from room import Room
from User import User

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#313338")  # Set a background color
        self.configure(padx=20, pady=20)  # Increase padding around the frame

        #set the background color for the label using a hexadecimal color code
        label = tk.Label(self, text="Login", font=("Helvetica",   20), fg="#f2f3f5", bg="#313338")
        label.pack(pady=10)
        
        # input and input display
        username_label = tk.Label(self, text="Pseudo", font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")
        username_label.pack()

        self.username_entry = tk.Entry(self, font=("Helvetica",  14))  # Increase font size
        self.username_entry.pack()

        password_label = tk.Label(self, text="Password", font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")
        password_label.pack()

        self.password_entry = tk.Entry(self, show="*", font=("Helvetica",  14))  # Increase font size
        self.password_entry.pack()

        #button to login
        login_button = tk.Button(self, text="Login", command=lambda: self.login(controller), font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")
        login_button.pack(pady=10)

        #button to creat a new acount
        new_acount_button = tk.Button(self, text="Inscription", command=lambda: controller.show_frame(Acount_creation), font=("Helvetica",  14), fg="#f2f3f5", bg="#313338")
        new_acount_button.pack(pady=10)

    #loongin fonction
    def login(self, controller):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        test_user = User()
        user_info = test_user.read_user_pseudo(username)
        if password == user_info[0][4]:
            messagebox.showinfo("conexion", "Bien venue!")
            # Correctly pass an instance of the Room class with the username
            controller.show_frame(Room)
        else :
            messagebox.showinfo("ereur", "Information incorect!")


