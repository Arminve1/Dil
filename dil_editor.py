import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font, ttk
import os
import random

class DilEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.font_size = 12
        self.font = font.Font(family="TkDefaultFont", size=self.font_size)
        self.title("Dil")
        self.geometry("800x600")
        self.dark_mode = tk.BooleanVar(value=False)
        self.tabs = {}
        self._create_widgets()
        self.apply_theme()
        self.bind("<Control-n>", lambda e: self.new_tab())
        self.bind("<Control-o>", lambda e: self.open_file())
        self.bind("<Control-s>", lambda e: self.save_file())
        self.bind("<Control-plus>", lambda e: self.increase_font_size())
        self.bind("<Control-minus>", lambda e: self.decrease_font_size())
        self.bind("<Control-f>", lambda e: self.find_text())
        self.bind("<Control-Shift-H>", lambda e: self.show_secret())

    def _create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.status = tk.Label(self, text="New file", anchor='w')
        self.status.pack(fill=tk.X, side=tk.BOTTOM)

        self.new_tab()

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Tab", command=self.new_tab)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_command(label="Close Tab", command=self.close_tab)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.current_text().event_generate('<<Cut>>'))
        edit_menu.add_command(label="Copy", command=lambda: self.current_text().event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda: self.current_text().event_generate('<<Paste>>'))
        edit_menu.add_command(label="Select All", command=lambda: self.current_text().event_generate('<<SelectAll>>'))
        edit_menu.add_separator()
        edit_menu.add_command(label="Find", command=self.find_text)
        edit_menu.add_command(label="Word Count", command=self.show_word_count)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        insert_menu = tk.Menu(menubar, tearoff=0)
        insert_menu.add_command(label="Image", command=self.insert_image)
        menubar.add_cascade(label="Insert", menu=insert_menu)

        game_menu = tk.Menu(menubar, tearoff=0)
        game_menu.add_command(label="Guess Number", command=self.start_game)
        menubar.add_cascade(label="Game", menu=game_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Increase Font Size", command=self.increase_font_size)
        view_menu.add_command(label="Decrease Font Size", command=self.decrease_font_size)
        view_menu.add_checkbutton(label="Dark Mode", onvalue=True, offvalue=False,
                                  variable=self.dark_mode, command=self.apply_theme)
        menubar.add_cascade(label="View", menu=view_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Credits", command=self.show_credits)
        help_menu.add_command(label="Surprise", command=self.show_secret)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    def apply_theme(self):
        for tab in self.tabs.values():
            widget = tab["text"]
            if self.dark_mode.get():
                widget.config(bg="#1e1e1e", fg="white", insertbackground="white")
            else:
                widget.config(bg="white", fg="black", insertbackground="black")
        if self.dark_mode.get():
            self.status.config(bg="#2e2e2e", fg="white")
        else:
            self.status.config(bg=self.cget("bg"), fg="black")

    def update_status(self, text):
        self.status.config(text=text)

    def current_tab(self):
        sel = self.notebook.select()
        if not sel:
            return None
        frame = self.notebook.nametowidget(sel)
        return self.tabs.get(frame)

    def current_text(self):
        tab = self.current_tab()
        return tab["text"] if tab else None

    def new_tab(self):
        frame = tk.Frame(self.notebook)
        text = tk.Text(frame, font=self.font)
        text.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(frame, text="Untitled")
        self.notebook.select(frame)
        self.tabs[frame] = {"text": text, "filepath": None, "images": []}
        self.apply_theme()
        self.update_status("New file")

    def close_tab(self):
        sel = self.notebook.select()
        if sel:
            frame = self.notebook.nametowidget(sel)
            self.notebook.forget(frame)
            self.tabs.pop(frame, None)

    def open_file(self):
        filepath = filedialog.askopenfilename(defaultextension=".vdad",
                                              filetypes=[("VDAD files", "*.vdad"), ("All files", "*.*")])
        if filepath:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    contents = f.read()
                self.new_tab()
                tab = self.current_tab()
                tab["text"].insert(tk.END, contents)
                tab["filepath"] = filepath
                self.notebook.tab(self.notebook.select(), text=os.path.basename(filepath))
                self.update_status(os.path.basename(filepath))
            except OSError as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        tab = self.current_tab()
        if not tab:
            return
        if tab["filepath"]:
            try:
                with open(tab["filepath"], 'w', encoding='utf-8') as f:
                    f.write(tab["text"].get(1.0, tk.END))
                self.update_status(os.path.basename(tab["filepath"]))
            except OSError as e:
                messagebox.showerror("Error", str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        tab = self.current_tab()
        if not tab:
            return
        filepath = filedialog.asksaveasfilename(defaultextension=".vdad",
                                                filetypes=[("VDAD files", "*.vdad"), ("All files", "*.*")])
        if filepath:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(tab["text"].get(1.0, tk.END))
                tab["filepath"] = filepath
                self.notebook.tab(self.notebook.select(), text=os.path.basename(filepath))
                self.update_status(os.path.basename(filepath))
            except OSError as e:
                messagebox.showerror("Error", str(e))

    def increase_font_size(self):
        self.font_size += 1
        self.font.configure(size=self.font_size)
        for tab in self.tabs.values():
            tab["text"].configure(font=self.font)

    def decrease_font_size(self):
        if self.font_size > 1:
            self.font_size -= 1
            self.font.configure(size=self.font_size)
            for tab in self.tabs.values():
                tab["text"].configure(font=self.font)

    def find_text(self):
        term = simpledialog.askstring("Find", "Text to find:")
        if term:
            text = self.current_text()
            start = text.search(term, "1.0", tk.END)
            if start:
                end = f"{start}+{len(term)}c"
                text.tag_remove("found", "1.0", tk.END)
                text.tag_add("found", start, end)
                text.tag_config("found", background="yellow")
                text.see(start)
            else:
                messagebox.showinfo("Find", "Text not found.")

    def insert_image(self):
        tab = self.current_tab()
        if not tab:
            return
        filepath = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.gif"), ("All files", "*.*")]
        )
        if filepath:
            try:
                img = tk.PhotoImage(file=filepath)
                tab["text"].image_create(tk.INSERT, image=img)
                tab["images"].append(img)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def show_word_count(self):
        tab = self.current_tab()
        if tab:
            text = tab["text"].get(1.0, tk.END)
            words = len(text.split())
            messagebox.showinfo("Word Count", f"{words} words")

    def start_game(self):
        GuessGame(self)

    def show_credits(self):
        top = tk.Toplevel(self)
        top.title("Credits")
        tk.Label(top, text="Arming-Studios.com").pack(padx=20, pady=20)

    def show_secret(self):
        messagebox.showinfo("Secret", "Danke dass du Dil verwendest!")


class GuessGame(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Guess the Number")
        self.number = random.randint(1, 100)
        tk.Label(self, text="Guess a number between 1 and 100").pack(padx=10, pady=10)
        self.entry = tk.Entry(self)
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", self.check)
        self.result = tk.Label(self, text="")
        self.result.pack(padx=10, pady=10)

    def check(self, event=None):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result.config(text="Please enter a number")
            return
        if guess < self.number:
            self.result.config(text="Too low")
        elif guess > self.number:
            self.result.config(text="Too high")
        else:
            self.result.config(text="Correct!")

if __name__ == "__main__":
    app = DilEditor()
    app.mainloop()
