import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Editor")

        self.textarea = tk.Text(self.window, font=("Helvetica", 12))
        self.textarea.pack(expand=True, fill='both')

        self.menu = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.window.config(menu=self.menu)
        self.window.mainloop()

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(default=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.textarea.delete(1.0, tk.END)
                    self.textarea.insert(1.0, file.read())
            except Exception as e:
                messagebox.showerror("Error", e)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(default=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.textarea.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", e)

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def exit(self):
        self.window.destroy()

if __name__ == '__main__':
    TextEditor()
