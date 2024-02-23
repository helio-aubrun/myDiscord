import tkinter as tk
from tkinter import messagebox
import tkinter as tk
import login
import User

class Acount_creation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#313338")
        label = tk.Label(self, text="inscription", fg="#f2f3f5", bg="#313338")
        label.pack(pady=10, padx=10)
        
        nom_label = tk.Label(self, text="nom", fg="#f2f3f5", bg="#313338")
        nom_label.pack()

        self.nom_entry = tk.Entry(self)
        self.nom_entry.pack()

        prenom_label = tk.Label(self, text="preonm", fg="#f2f3f5", bg="#313338")
        prenom_label.pack()

        self.prenom_entry = tk.Entry(self)
        self.prenom_entry.pack()

        pseudo_label = tk.Label(self, text="psudo", fg="#f2f3f5", bg="#313338")
        pseudo_label.pack()

        self.pseudo_entry = tk.Entry(self)
        self.pseudo_entry.pack()

        email_label = tk.Label(self, text="email", fg="#f2f3f5", bg="#313338")
        email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        mot_de_passe_label = tk.Label(self, text="mot de passe", fg="#f2f3f5", bg="#313338")
        mot_de_passe_label.pack()

        self.mot_de_passe_entry = tk.Entry(self, show="*")
        self.mot_de_passe_entry.pack()

        

        """password_label = tk.Label(self, text="Password")
        password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()"""

        login_button = tk.Button(self, text="Login", command=lambda: self.new_acount (controller), fg="#f2f3f5", bg="#313338")
        login_button.pack()

        back_button = tk.Button(self, text="Back to Login", command=lambda: self.go_back_to_login(controller), fg="#f2f3f5", bg="#313338")
        back_button.pack()

    def go_back_to_login(self, controller):
        controller.show_frame(login.Login)

    def new_acount (self, controller):
        if not self.are_fields_filled () :
            messagebox.showerror("Creation echouer", "Veller remplire tous les case.")
        else :
            new_user = User.user
            new_user.add_user (self.nom_entry, self.prenom_entry, self.pseudo_entry, self.email_entry, self.mot_de_passe_entry)
    
    def are_fields_filled(self):
        fields = [self.nom_entry, self.prenom_entry, self.pseudo_entry, self.email_entry, self.mot_de_passe_entry]
        for field in fields:
            if field.get() == "":
                return False
        return True

