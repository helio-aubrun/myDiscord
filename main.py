import tkinter as tk
from login import Login  # Import the custom frame class
from acount_creation import Acount_creation

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")  # Set the window size to  800x600

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Acount_creation, Login):  # Add the custom frame to the list of frames
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class new_acount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the main page")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Go to Custom Frame",
                           command=lambda: controller.show_frame(Acount_creation))
        button.pack()

if __name__ == "__main__":
    app = Main()
    app.mainloop()
