import tkinter as tk
from tkinter import messagebox
import csv
import os
from pynput import mouse

class MouseRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Click Recorder")
        self.root.attributes("-topmost", True)  # Set the window to be always on top

        # CSV File name
        self.filename = "mouse_clicks.csv"

        # Load existing data from the CSV file
        self.data = None

        # Mouse Listener
        self.listener = mouse.Listener(on_click=self.on_click)
        self.clicks = []  # List to store mouse click positions

        # GUI Setup
        self.setup_gui()

    def setup_gui(self):
        """Setup the GUI components."""
        self.key_label = tk.Label(self.root, text="Enter Key Name:")
        self.key_label.pack(pady=5)

        self.key_entry = tk.Entry(self.root)
        self.key_entry.pack(pady=5)

        self.record_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.show_button = tk.Button(self.root, text="Show Data", command=self.show_data)
        self.show_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def load_from_csv(self):
        """Load data from a CSV file into a dictionary."""
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if len(row) > 1:  # Ensure the row has at least 2 elements (key and positions)
                        key, *positions = row
                        data[key] = eval(positions[0]) if positions else []
        return data

    def save_to_csv(self):
        """Save the current dictionary to a CSV file."""
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            self.clicks.pop(-1)
            writer.writerow([self.key, self.clicks])
            # for key, positions in self.data.items():
            #      self.data[key].pop(-1)
            #      writer.writerow([key, positions])

    def on_click(self, x, y, button, pressed):
        """Record the mouse click position."""
        if pressed:
            self.clicks.append((x, y))
            print(f"Recorded click at: ({x}, {y})")

    def start_recording(self):
        """Start recording mouse clicks."""
        self.key = self.key_entry.get().strip()
        if not self.key:
            messagebox.showwarning("Input Error", "Please enter a key name.")
            return

        self.clicks = []  # Reset clicks list
        self.listener.start()
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        print("Recording started...")

    def stop_recording(self):
        """Stop recording and save the data."""
        self.listener.stop()
        #key = self.key_entry.get().strip()
        #if key in self.data:
        #     self.data[key].extend(self.clicks)  # Append new clicks to existing data
        # else:
        #     self.data[key] = self.clicks

        self.save_to_csv()
        messagebox.showinfo("Success", f"Recorded {len(self.clicks)} clicks for key '{self.key}'.")
        self.key_entry.delete(0, tk.END)
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        print("Recording stopped.")


    def show_data(self):
        """Display the contents of the data."""
        if not self.data : self.data = self.load_from_csv()
        if self.data:
            data_str = "\n".join(f"{key}: {positions}" for key, positions in self.data.items())
            messagebox.showinfo("Data Contents", data_str)
        else:
            messagebox.showinfo("Data Contents", "No data recorded yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseRecorderApp(root)
    root.mainloop()
