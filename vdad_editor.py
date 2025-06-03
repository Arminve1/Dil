import tkinter as tk
from tkinter import filedialog, messagebox
import os

class VdadEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VDAD Editor")
        self.geometry("800x600")
        self._create_widgets()
        self.filepath = None

    def _create_widgets(self):
        self.text_area = tk.Text(self)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        menubar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menubar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filepath = None

    def open_file(self):
        filepath = filedialog.askopenfilename(defaultextension=".vdad",
                                              filetypes=[("VDAD files", "*.vdad"), ("All files", "*.*")])
        if filepath:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    contents = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, contents)
                self.filepath = filepath
            except OSError as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        if self.filepath:
            try:
                with open(self.filepath, 'w', encoding='utf-8') as f:
                    f.write(self.text_area.get(1.0, tk.END))
            except OSError as e:
                messagebox.showerror("Error", str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".vdad",
                                                filetypes=[("VDAD files", "*.vdad"), ("All files", "*.*")])
        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(self.text_area.get(1.0, tk.END))
                self.filepath = filepath
            except OSError as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = VdadEditor()
    app.mainloop()
