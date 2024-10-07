import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button, Menu, messagebox
from tkinter import *


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Bob\'s notepad')
        self.current_file_path = None

        # Text widget
        self.text_area = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')


        # label widget
        self.label = Label(self.root, text='geeks')
        self.label.pack()


        # Frame 
        self.button_frame = Frame(self.root)
        self.button_frame.pack()


        # Menu
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_file)

        # Save as button
        self.save_as_button = Button(self.button_frame, text='Save As', command=self.save_as_file)
        self.save_as_button.pack(side=tk.LEFT)

        # Save button
        self.save_button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Load button
        self.load_button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)


    def save_file(self) -> None:
        if self.current_file_path:
            with open(self.current_file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Save", "File saved successfully!")
        else:
            self.save_as_file()


    def save_as_file(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                 filetypes=[('Text files', '*.txt')])
        
        with open(file_path, 'w') as file:
             file.write(self.text_area.get(1.0, tk.END))

        self.current_file_path = file_path

        print(f'File saved to {file_path}')


    def load_file(self) -> None:
        file_path = filedialog.askopenfilename(defaultextension='.txt',
                                                filetypes=[('Text files', '*.txt')])

        with open(file_path, 'r') as file:
            content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)

        self.current_file_path = file_path

        print(f'file loaded from {file_path}')                     


    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root = tk.Tk()
    app = SimpleNotepad(root=root)
    app.run()


if __name__ == '__main__':
    main()





