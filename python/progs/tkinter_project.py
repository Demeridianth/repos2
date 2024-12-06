import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button, Menu, messagebox
from tkinter import *


def main():
    window = Tk()
    window.title('Notepad')

    def save_file():
        global current_file_path
        if current_file_path:
            with open(current_file_path, 'w') as file:
                file.write(text.get(1.0, tk.END))
            messagebox.showinfo('Save', 'File saved successfully!')
        else:
            save_as_file()

    def save_as_file():
        global current_file_path
        file_path = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[
                ('Text Files', '.txt'),
                ('Python Files', '.py'),
                ('HTML Files', '.html'),
                ('All Files', '*.*')
            ]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get(1.0, tk.END))
            messagebox.showinfo('Save as', 'File saved succesfuly')
            current_file_path = file_path

    def open_file():
        global current_file_path
        file_path = filedialog.askopenfilename(
            defaultextension='.txt',
            filetypes=[
                ('Text Files', '.txt'),
                ('Python Files', '.py'),
                ('HTML Files', '.html'),
                ('All Files', '*.*')
            ]
        )
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
            current_file_path = file_path

    def delete_button():
        text.delete(1.0, tk.END)


    # WIDGETS


    # label
    label = tk.Label()
    label.pack()

    # text
    text = Text(window, wrap='word', undo=True)
    text.pack(expand=True, fill='both')


    # frame
    frame = Frame(window)
    frame.pack()

    #  delete all text button
    delete = Button(frame, text='Clear', command=delete_button)
    delete.pack(side=tk.LEFT)
    

    # menu bar
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # file menu
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='File', menu=file_menu)
    # commands
    file_menu.add_command(label='Open', command=open_file)
    file_menu.add_command(label='Save', command=save_file)
    file_menu.add_command(label='Save As', command=save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=window.quit)

    # edit menu
    edit_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Edit', menu=edit_menu)
    # commands
    edit_menu.add_command(label='Undo', command=text.edit_undo)
    edit_menu.add_command(label='Redo', command=text.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_command(label='Cut', command=lambda: text.event_generate('<<Cut>>'))
    edit_menu.add_command(label='Copy', command=lambda: text.event_generate('<<Copy>>'))
    edit_menu.add_command(label='Paste', command=lambda: text.event_generate('<<Paste>>'))
    edit_menu.add_command(label='Delete', command=lambda: text.delete('sel.first', 'sel.last'))


    window.mainloop()


current_file_path = None


if __name__ == '__main__':
    main()