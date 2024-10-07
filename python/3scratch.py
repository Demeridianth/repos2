import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button, Menu, messagebox
from tkinter import *


def main():
    window = Tk()
    window.title('No\' tepap')


    # WIDGETS

    # label
    label = tk.Label(text='frame')
    label.pack()

    # text
    text = Text(window, wrap='word')
    text.pack(expand=True, fill='both')


    # frame
    frame = Frame(window)
    frame.pack()

    #  1 button
    button1 = Button(frame, text='111')
    button1.pack(side=tk.LEFT)
    #  2 button
    button2 = Button(frame, text='222')
    button2.pack(side=tk.LEFT)


    # menu bar
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # file menu
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='File', menu=file_menu)
    
    # file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    # file_menu.add_command(label="Save As", command=save_as_file)
    # file_menu.add_separator()
    # file_menu.add_command(label="Exit", command=window.quit)


    # commands

    def save_file():
        global current_file_path
        if current_file_path



    current_file_path = None
    window.mainloop()


if __name__ == '__main__':
    main()