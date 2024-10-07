import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)  # Clear any existing content
            text_area.insert(tk.END, file.read())  # Insert the file content into the Text widget
        window.title(f"Editing - {file_path}")  # Update window title with file name
        return file_path
    return None

def save_file():
    if current_file_path:  # Only if the file path exists
        with open(current_file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))  # Save the current content of the Text widget
        messagebox.showinfo("Save", "File saved successfully!")
    else:
        save_as_file()

def save_as_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))  # Save the current content of the Text widget
        messagebox.showinfo("Save As", "File saved successfully!")
        window.title(f"Editing - {file_path}")  # Update window title with file name
        return file_path
    return None

# Setup the window
window = tk.Tk()
window.title("Simple Text Editor")

# Text Area
text_area = tk.Text(window, wrap="word")
text_area.pack(expand=1, fill="both")

# Menu Bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

current_file_path = None  # Variable to store the current file path

# Run the application
window.mainloop()
