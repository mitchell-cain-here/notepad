import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import filedialog as fd

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                text_content = text_widget.get("1.0", "end-1c")
                file.write(text_content)
            status_label.config(text=f"File saved: {file_path}")
        except Exception as e:
            status_label.config(text=f"Error saving file: {str(e)}")

root = tk.Tk()
root.title("Mitchell's Text Editor")
root.configure(bg="#000000")

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.pack(padx=20, pady=20, fill="both", expand=True)

save_button = tk.Button(root, text="Save", command=save_to_file)
save_button.pack(pady=10)

status_label = tk.Label(root, text="", padx=10, pady=10, bg="#000000")
status_label.pack()

def open_text_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    f = fd.askopenfile(filetypes=filetypes)
    text_widget.insert('1.0', f.readlines())

# To Do - Make this clear text after opening a file and adjust button height 
open_button = tk.Button(root,text='Open a File',command=open_text_file)
open_button.pack(pady=10)
root.mainloop()