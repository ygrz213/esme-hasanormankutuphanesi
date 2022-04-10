import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme = 'arc')
root.wm_iconbitmap('icons/book.ico')

button_frame = tk.Frame()
button_frame.pack(side = 'top', fill = 'x')

add_book_icon = tk.PhotoImage(file = 'icons/plus.png')
add_book = ttk.Button(button_frame, text = '   Kitap ekle', image = add_book_icon, compound = 'left')
add_book.pack(side = 'left', ipadx = 3, ipady = 1)

lent_books_icon = tk.PhotoImage(file = 'icons/lend.png')
lent_books = ttk.Button(button_frame, text = 'Ödünç verilmiş kitaplar', image = lent_books_icon, compound = 'top')
lent_books.pack(side = 'top', ipadx = 3, ipady = 1)


root.mainloop()
