import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font
import os

class DilEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.font_size = 12
        self.font = font.Font(family="TkDefaultFont", size=self.font_size)
        self.title("Dil")
        self.geometry("800x600")
        self._create_widgets()
        self.filepath = None
        self.bind("<Control-n>", lambda e: self.new_file())
        self.bind("<Control-o>", lambda e: self.open_file())
        self.bind("<Control-s>", lambda e: self.save_file())
        self.bind("<Control-plus>", lambda e: self.increase_font_size())
        self.bind("<Control-minus>", lambda e: self.decrease_font_size())
        self.bind("<Control-f>", lambda e: self.find_text())

    def _create_widgets(self):
        self.text_area = tk.Text(self, font=self.font)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate('<<Cut>>'))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate('<<Paste>>'))
        edit_menu.add_command(label="Select All", command=lambda: self.text_area.event_generate('<<SelectAll>>'))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=self.find_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Increase Font Size", command=self.increase_font_size)
        view_menu.add_command(label="Decrease Font Size", command=self.decrease_font_size)
        menubar.add_cascade(label="View", menu=view_menu)

        self.config(menu=menubar)

        self.status = tk.Label(self, text="New file", anchor='w')
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

    def update_status(self, text):
        self.status.config(text=text)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filepath = None
        self.update_status("New file")

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
                self.update_status(os.path.basename(filepath))
            except OSError as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        if self.filepath:
            try:
                with open(self.filepath, 'w', encoding='utf-8') as f:
                    f.write(self.text_area.get(1.0, tk.END))
                self.update_status(os.path.basename(self.filepath))
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
                self.update_status(os.path.basename(filepath))
            except OSError as e:
                messagebox.showerror("Error", str(e))

    def increase_font_size(self):
        self.font_size += 1
        self.font.configure(size=self.font_size)

    def decrease_font_size(self):
        if self.font_size > 1:
            self.font_size -= 1
            self.font.configure(size=self.font_size)

    def find_text(self):
        term = simpledialog.askstring("Find", "Text to find:")
        if term:
            start = self.text_area.search(term, "1.0", tk.END)
            if start:
                end = f"{start}+{len(term)}c"
                self.text_area.tag_remove("found", "1.0", tk.END)
                self.text_area.tag_add("found", start, end)
                self.text_area.tag_config("found", background="yellow")
                self.text_area.see(start)
            else:
                messagebox.showinfo("Find", "Text not found.")

if __name__ == "__main__":
    app = DilEditor()
    app.mainloop()
