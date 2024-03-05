import tkinter as tk
from tkinter import ttk

class Pricate_room :
    def run (self, root) :

        # Calculate the width of the Listbox and the remaining frame
        screen_width = root.winfo_screenwidth()
        listbox_width = int(screen_width *   0.2)
        remaining_width = screen_width - listbox_width

        # Create the Listbox with a horizontal Scrollbar
        scrollbar = ttk.Scrollbar(root, orient='horizontal')
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        listbox = tk.Listbox(root, xscrollcommand=scrollbar.set, width=listbox_width)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure the Scrollbar to update the Listbox
        scrollbar.config(command=listbox.xview)

        # Create a Frame to hold the remaining content
        content_frame = tk.Frame(root)
        content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        # Populate the Listbox with some items
        for i in range(100):
            listbox.insert(tk.END, f"Item {i}")
