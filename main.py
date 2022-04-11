import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

class application():
    def __init__(self, master):
        button_frame = tk.Frame(master)
        button_frame.pack(side = 'top', fill = 'x')

        global add_book_icon; add_book_icon = tk.PhotoImage(file = 'icons/plus.png')
        add_book = ttk.Button(button_frame, text = '   Kitap ekle', image = add_book_icon, compound = 'left')
        add_book.pack(side = 'left', ipadx = 4, ipady = 2)

        global search_book_icon; search_book_icon = tk.PhotoImage(file = 'icons/search.png')
        search_book = ttk.Button(button_frame, text = 'Kitap ara   ', image = search_book_icon, compound = 'right')
        search_book.pack(side = 'right', ipadx = 3, ipady = 1)

        global lent_books_icon; lent_books_icon = tk.PhotoImage(file = 'icons/lend.png')
        lent_books = ttk.Button(button_frame, text = 'Ödünç verilmiş kitaplar', image = lent_books_icon, compound = 'top')
        lent_books.pack(side = 'top', ipadx = 3, ipady = 1)

root = ThemedTk(theme = 'arc')
widgets = application(root)
root.mainloop()