import tkinter as tk
from tkinter import messagebox, scrolledtext

from validator import validate_names
from calculator import calculate_compatibility
from history_manager import add_to_history, get_history, clear_history
from utils import format_result


class FriendshipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Friendship Compatibility Analyzer")
        
        # Make the window full screen
        self.root.attributes('-fullscreen', True)
        
        # Allow exiting full screen with Escape key
        self.root.bind("<Escape>", self.exit_fullscreen)
        
        self.root.configure(bg="#f0f4f8")

        self.create_widgets()

    def exit_fullscreen(self, event=None):
        """Exit full screen mode when Escape is pressed"""
        self.root.attributes('-fullscreen', False)
        self.root.geometry("520x580")
        self.root.resizable(True, True)

    def create_widgets(self):
        # Title
        title = tk.Label(
            self.root,
            text="Friendship Compatibility Analyzer",
            font=("Arial", 16, "bold"),
            bg="#f0f4f8",
            fg="#1a365d"
        )
        title.pack(pady=15)

        # Name 1
        tk.Label(self.root, text="Enter First Name:", font=("Arial", 11), bg="#f0f4f8").pack()
        self.entry1 = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.entry1.pack(pady=5)

        # Name 2
        tk.Label(self.root, text="Enter Second Name:", font=("Arial", 11), bg="#f0f4f8").pack()
        self.entry2 = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.entry2.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f0f4f8")
        btn_frame.pack(pady=12)

        tk.Button(
            btn_frame,
            text="Check Compatibility",
            font=("Arial", 11, "bold"),
            bg="#38a169",
            fg="white",
            width=18,
            command=self.check_compatibility
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Clear",
            font=("Arial", 11),
            bg="#e53e3e",
            fg="white",
            width=10,
            command=self.clear_fields
        ).grid(row=0, column=1, padx=5)

        # Result Label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12),
            bg="#f0f4f8",
            fg="#2d3748",
            justify="center"
        )
        self.result_label.pack(pady=10)

        # History Section
        tk.Label(
            self.root,
            text="History of Previous Checks",
            font=("Arial", 11, "bold"),
            bg="#f0f4f8"
        ).pack(pady=(10, 5))

        self.history_box = scrolledtext.ScrolledText(
            self.root,
            width=55,
            height=10,
            font=("Arial", 10),
            state="disabled"
        )
        self.history_box.pack(pady=5)

        # History Buttons
        hist_btn_frame = tk.Frame(self.root, bg="#f0f4f8")
        hist_btn_frame.pack(pady=8)

        tk.Button(
            hist_btn_frame,
            text="Refresh History",
            font=("Arial", 10),
            command=self.load_history
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            hist_btn_frame,
            text="Clear History",
            font=("Arial", 10),
            bg="#c53030",
            fg="white",
            command=self.clear_history_action
        ).grid(row=0, column=1, padx=5)

        # Load history when app starts
        self.load_history()

    def check_compatibility(self):
        name1 = self.entry1.get()
        name2 = self.entry2.get()

        # Module 1: Validation
        is_valid, error_msg = validate_names(name1, name2)
        if not is_valid:
            messagebox.showerror("Invalid Input", error_msg)
            return

        # Module 2: Calculation
        percentage, message = calculate_compatibility(name1, name2)

        # Display result
        result_text = format_result(name1, name2, percentage, message)
        self.result_label.config(text=result_text)

        # Module 3: Save to history
        add_to_history(name1, name2, percentage, message)
        self.load_history()

    def clear_fields(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="")

    def load_history(self):
        history = get_history()
        self.history_box.config(state="normal")
        self.history_box.delete("1.0", tk.END)

        if not history:
            self.history_box.insert(tk.END, "No history yet.")
        else:
            for item in reversed(history):  # latest first
                self.history_box.insert(tk.END, item + "\n")

        self.history_box.config(state="disabled")

    def clear_history_action(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all history?")
        if confirm:
            clear_history()
            self.load_history()
            messagebox.showinfo("Done", "History cleared successfully.")
