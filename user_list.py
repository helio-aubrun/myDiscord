import tkinter as tk
from tkinter import ttk
from User import user
from database import Database

class User_list(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="#313338")  # Set a background color
        self.configure(padx=20, pady=20)  # Increase padding around the frame
        users = user(Database(host="localhost", user="root", password="2879", database="mydiscord"))
        user_data = users.read_all_user_public()
        print (user_data)

        # Create a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox
        self.listbox = tk.Listbox(self, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure the scrollbar
        scrollbar.config(command=self.listbox.yview)

        # Populate the listbox with users
        self.populate_listbox(user_data)

    def populate_listbox(self, user_data):
        # Assuming user_data.read_all_user() returns a list of users
        for user_info in user_data:
            self.listbox.insert(tk.END, user_info)
