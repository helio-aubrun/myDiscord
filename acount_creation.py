import tkinter as tk
from tkinter import messagebox
import tkinter as tk
import login
from User import User

# Class for account creation frame
class Acount_creation(tk.Frame):
    def __init__(self, parent, controller):
        # Initialize the frame with a background color
        tk.Frame.__init__(self, parent, bg="#313338")

        # Create a label for the account creation page
        label = tk.Label(self, text="inscription", fg="#f2f3f5", bg="#313338")
        label.pack(pady=10, padx=10)

        # Create and pack name label and entry
        nom_label = tk.Label(self, text="nom", fg="#f2f3f5", bg="#313338")
        nom_label.pack()
        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack()

        # Create and pack first name label and entry
        prenom_label = tk.Label(self, text="preonm", fg="#f2f3f5", bg="#313338")
        prenom_label.pack()
        self.prenom_entry = tk.Entry(self)
        self.prenom_entry.pack()

        # Create and pack username label and entry
        pseudo_label = tk.Label(self, text="pseudo", fg="#f2f3f5", bg="#313338")
        pseudo_label.pack()
        self.pseudo_entry = tk.Entry(self)
        self.pseudo_entry.pack()

        # Create and pack email label and entry
        email_label = tk.Label(self, text="email", fg="#f2f3f5", bg="#313338")
        email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        # Create and pack password label and entry
        mot_de_passe_label = tk.Label(self, text="mot de passe", fg="#f2f3f5", bg="#313338")
        mot_de_passe_label.pack()
        self.mot_de_passe_entry = tk.Entry(self, show="*")
        self.mot_de_passe_entry.pack()

        # Create and pack the account creation button
        login_button = tk.Button(self, text="inscription", command=lambda: self.new_acount (), fg="#f2f3f5", bg="#313338")
        login_button.pack()

        # Create and pack the back button
        back_button = tk.Button(self, text="Back to Login", command=lambda: self.go_back_to_login(controller), fg="#f2f3f5", bg="#313338")
        back_button.pack()

    # Method to navigate back to the login page
    def go_back_to_login(self, controller):
        controller.show_frame(login.Login)

    # Method to create a new account
    def new_acount (self):
        if not self.are_fields_filled () :
            messagebox.showerror("Creation echouer", "Veller remplire tous les case.")
        else :
            new_user = User()
            new_user.add_user (self.nom_entry.get(), self.prenom_entry.get(), self.pseudo_entry.get(), self.email_entry.get(), self.mot_de_passe_entry.get())

    # Method to check if all fields are filled
    def are_fields_filled(self):
        fields = [self.nom_entry, self.prenom_entry, self.pseudo_entry, self.email_entry, self.mot_de_passe_entry]
        for field in fields:
            if field.get() == "":
                return False
        return True
