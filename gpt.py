import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return

    editor.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        editor.insert(tk.END, text)
    
    main.title(f'Text Editor - {filepath}')

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = editor.get(1.0, tk.END)
        output_file.write(text)
    
    main.title(f'Text Editor - {filepath}')

# main window
main = tk.Tk()
main.title("Text Editor")
main.minsize(width=600, height=600)
main.rowconfigure(2, weight=2)
main.columnconfigure(2, weight=2)

# buttons
button_frame = tk.Frame(main, relief="groove")
button_frame.grid(column=0, row=0, sticky="ns")

open_file_button = ttk.Button(button_frame, text="Open File", command=open_file, width=15)
open_file_button.grid(column=0, row=0, sticky="nw")

save_file_button = ttk.Button(button_frame, text="Save As", command=save_file, width=15)
save_file_button.grid(column=0, row=1, sticky="nw")

# editor
editor = tk.Text(main, relief="groove", padx=5, wrap=tk.WORD, font=("Helvetica", 12))
editor.grid(column=2, row=0, sticky="nw")

main.mainloop()
