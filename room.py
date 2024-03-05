import tkinter as tk
from user_list import User_list
from message import Message
from channel import Channel

class Room(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#313338") # Set a background color
        self.configure(padx=20, pady=20) # Increase padding around the frame

        # Configure the main window to allow the frames to expand
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure(0, weight=1)

        # Create the first container with a scrollable list
        self.scrollable_list_container = tk.Frame(self, bg="#313338", width=200) # Set the width to 200 pixels
        self.scrollable_list_container.grid(row=0, column=0, sticky="nsew")

        # Create a canvas for the scrollable list
        self.canvas = tk.Canvas(self.scrollable_list_container, bg="#313338")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self.scrollable_list_container, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold the list items
        self.list_frame = tk.Frame(self.canvas, bg="#313338")
        self.canvas.create_window((0, 0), window=self.list_frame, anchor="nw")

        # Bind the configure method to the list_frame to update the scroll region
        self.list_frame.bind("<Configure>", self.on_configure)

        # Create the second container, which is empty
        self.empty_container = tk.Frame(self, bg="#313338")
        self.empty_container.grid(row=0, column=1, sticky="nsew")

        # Create the top container with a scrollable list
        self.top_container = tk.Frame(self.empty_container, bg="#313338")
        self.top_container.pack(side="top", fill="both", expand=True)

        # Create the bottom container with a text input zone and a button
        self.bottom_container = tk.Frame(self.empty_container, bg="#313338")
        self.bottom_container.pack(side="top", fill="x")

        # Text input zone
        self.text_input = tk.Entry(self.bottom_container, bg="#313338", fg="#f2f3f5")
        self.text_input.pack(side="left", fill="x", expand=True)

        # Button
        self.submit_button = tk.Button(self.bottom_container, text="Submit", bg="#313338", fg="#f2f3f5")
        self.submit_button.pack(side="right")

        #fill the channel list
        for i in range (Channel().get_channels_number ()):
            item = tk.Label(self.list_frame, text=f"Item {i}", bg="#313338", fg="#f2f3f5")
            item.pack(fill="x")
            item.bind("<Double-1>", self.on_item_double_click)


    def fill_top_scrollable_list(self, channel_id = 1):
        """Fills the top scrollable list with the given items."""
        items = Message.get_messages_channel (channel_id)
        for item_text in items:
            item = tk.Label(self.list_frame, text=item_text, bg="#313338", fg="#f2f3f5")
            item.pack(fill="x")
            item.bind("<Double-1>", self.on_item_double_click)
            
    def on_configure(self, event):
        # Update the scroll region when the list_frame is configured
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_item_double_click(self, event):
        # This method will be called when an item is double-clicked
        # You can access the widget that was clicked with event.widget
        # For example, to get the text of the clicked item:
        item_text = event.widget.cget("text")
        self.fill_top_scrollable_list(channel_id = item_text)
        # Add your custom logic here
