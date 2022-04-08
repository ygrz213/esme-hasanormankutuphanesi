import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme = 'arc')
root.wm_iconbitmap('icons/book.ico')

add_book_icon = tk.PhotoImage(file = 'icons/plus.png')
add_book = ttk.Button(text = '   Kitap ekle', image = add_book_icon, compound = 'left')
add_book.grid(padx = (35,0), ipady = 3, ipadx = 1)

root.mainloop()
