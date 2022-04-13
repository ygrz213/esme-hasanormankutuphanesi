from tkinter import ttk
from shutil import rmtree
from ttkthemes import ThemedTk
import tkinter as tk
import book_handler as bkh

class application():
    def __init__(self, master):
        self.master = master
        self.master.wm_iconbitmap('icons/book.ico')
        self.master.title('Esme Hasan ve Orman Kütüphanesi')
        self.master.protocol('WM_DELETE_WINDOW', self.delete_cache)

        self.widgets()

    def widgets(self):
        button_frame = tk.Frame(self.master)
        button_frame.pack(side = 'top', fill = 'x')

        global add_book_icon; add_book_icon = tk.PhotoImage(file = 'icons/plus.png')
        add_book = ttk.Button(button_frame,
                              text = '   Kitap ekle',
                              image = add_book_icon,
                              compound = 'left',
                              command = bkh.add_book_gui)
        add_book.pack(side = 'left', ipadx = 4, ipady = 2)

        global search_book_icon; search_book_icon = tk.PhotoImage(file = 'icons/search.png')
        search_book = ttk.Button(button_frame,
                                 text = 'Kitap ara   ',
                                 image = search_book_icon,
                                 compound = 'right')
        search_book.pack(side = 'right', ipadx = 3, ipady = 1)

        global lent_books_icon; lent_books_icon = tk.PhotoImage(file = 'icons/lend.png')
        lent_books = ttk.Button(button_frame,
                                text = 'Ödünç verilmiş kitaplar',
                                image = lent_books_icon,
                                compound = 'top')
        lent_books.pack(side = 'top', ipadx = 3, ipady = 1)

    def delete_cache(self):
        try:
            rmtree('__pycache__')
        except FileNotFoundError:
            pass
        self.master.destroy()

root = ThemedTk(theme = 'arc')
setup = application(root)
root.mainloop()