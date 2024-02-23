import tkinter as tk
from user_list import User_list  # Import the UserListFrame class

class Room(tk.Frame):
    def __init__(self, parent, controller):
        # Convert RGB values to hexadecimal color code
        bg_color = "#1E1E1E"  # This is the hexadecimal equivalent of RGB(30,  30,  30)
        tk.Frame.__init__(self, parent, bg="#313338")  # Set a background color
        self.configure(padx=20, pady=20)  # Increase padding around the frame

        # Configure the main window to allow the frames to expand
        self.grid_columnconfigure(0, weight=1)  # Allow the first column to expand more
        self.grid_columnconfigure(1, weight=5)  # Allow the second column to expand less
        self.grid_rowconfigure(0, weight=1)  # Allow the first row to expand

        # Step  3: Create the first frame
        frame1 = tk.Frame(self, bg="blue", width=80)

        # Step  4: Add the first frame to the container (main window)
        frame1.grid(row=0, column=0, sticky="nsew")

        # Step  5: Create the second frame
        frame2 = tk.Frame(self, bg="red")

        # Step  6: Add the second frame to the container (main window)
        frame2.grid(row=0, column=1, sticky="nsew")

        # Step  7: Create an instance of the UserListFrame and add it to frame1
        user_list_frame = User_list(frame1)  # Assuming UserListFrame takes a parent widget as an argument
        user_list_frame.pack(fill=tk.BOTH, expand=True)  # Adjust the packing options as needed

