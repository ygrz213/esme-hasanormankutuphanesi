from shutil import rmtree
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk
import book_handler as bkh
import database_handler as dbh
import table_handler as tbh

class application():
    def __init__(self, master):
        self.master = master
        self.master.wm_iconbitmap('icons/book.ico')
        self.master.title('Esme - Hasan Orman Kütüphanesi')
        self.master.protocol('WM_DELETE_WINDOW', self.delete_cache)

        self.widgets()

    def widgets(self):
        button_frame = tk.Frame(self.master)
        button_frame.pack(side = 'top', fill = 'x')

        self.add_book_icon = tk.PhotoImage(file = 'icons/plus.png')
        add_book = ttk.Button(button_frame,
                              text = '   Kitap ekle',
                              image = self.add_book_icon,
                              compound = 'left',
                              command = lambda: bkh.add_book_gui(self.table_tree))
        add_book.pack(side = 'left', ipadx = 4, ipady = 2)

        self.search_book_icon = tk.PhotoImage(file = 'icons/search.png')
        search_book = ttk.Button(button_frame,
                                 text = 'Kitap ara   ',
                                 image = self.search_book_icon,
                                 compound = 'right',
                                 command = lambda: bkh.search_book_gui(self.table_tree))
        search_book.pack(side = 'right', ipadx = 3, ipady = 1)

        self.lent_books_icon = tk.PhotoImage(file = 'icons/lend.png')
        lent_books = ttk.Button(button_frame,
                                text = 'Ödünç verilmiş kitaplar',
                                image = self.lent_books_icon,
                                compound = 'top')
        lent_books.pack(side = 'top', ipadx = 3, ipady = 1)

        self.genre = ttk.Combobox(values = ['Çocuk', 'Dinî', 'Hikâye', 'Roman', 'Şiir', 'Tarihî', 'Yetişkin'],
                                  state = 'readonly')
        self.genre.bind('<<ComboboxSelected>>', lambda x: tbh.filter_table_by_genre(self.genre.get(), self.table_tree))
        self.genre.pack(side = 'right', anchor = 'nw')
        tk.Label(text = 'Filtre:', bg = 'SystemButtonFace').pack(padx = 3, side = 'right', anchor = 'nw')

        self.table_tree = ttk.Treeview(columns = ('Tür', 'Numara', 'Kitap adı', 'Yazar veya Çeviren'), show = 'headings')
        self.table_tree.heading('Tür', text = 'Tür'); self.table_tree.heading('Numara', text = 'Numara'); self.table_tree.heading('Kitap adı', text = 'Kitap adı'); self.table_tree.heading('Yazar veya Çeviren', text = 'Yazar veya Çeviren')
        self.table_tree.column('Tür', anchor = 'center'); self.table_tree.column('Numara', anchor = 'center'); self.table_tree.column('Kitap adı', anchor = 'center'); self.table_tree.column('Yazar veya Çeviren', anchor = 'center')
        self.table_tree.bind('<Button-3>', self.pop_up)
        self.table_tree.pack(fill = 'both', expand = True)

    def pop_up(self, event):
        menu = tk.Menu(tearoff = 0)
        menu.add_command(label = 'Düzenle', command = lambda: bkh.edit_book_gui(self.table_tree))
        menu.add_command(label = 'Sil', command = lambda: [dbh.dbhandler.delete_book(self.table_tree.item(self.table_tree.selection())['values']), tbh.filter_table_by_genre(self.genre.get(), self.table_tree)])
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    def delete_cache(self):
        try:
            rmtree('__pycache__')
        except FileNotFoundError:
            pass
        self.master.destroy()

root = ThemedTk(theme = 'arc')

setup = application(root)
ttk.Style().configure('Bold.TButton', font = 'Helvetica 10 bold')

root.mainloop()