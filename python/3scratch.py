import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button
from tkinter import *


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Bob\'s notepad')

        # Text widget
        self.text_area = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')


        # label widget
        self.label = Label(self.root, text='geeks')
        self.label.pack()


        # Frame 
        self.button_frame = Frame(self.root)
        self.button_frame.pack()

        # Save button
        self.save_button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Load button
        self.load_button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)



    def save_file(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension='txt',)


    def load_file(self) -> None:
            pass


    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root = tk.Tk()
    app = SimpleNotepad(root=root)
    app.run()


if __name__ == '__main__':
    main()