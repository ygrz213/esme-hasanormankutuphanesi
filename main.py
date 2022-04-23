from tkinter import ttk
from shutil import rmtree
from ttkthemes import ThemedTk
import tkinter as tk
import book_handler as bkh
import table_handler as tbh

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
                                 compound = 'right',
                                 command = lambda: bkh.search_book_gui(table_tree))
        search_book.pack(side = 'right', ipadx = 3, ipady = 1)

        global lent_books_icon; lent_books_icon = tk.PhotoImage(file = 'icons/lend.png')
        lent_books = ttk.Button(button_frame,
                                text = 'Ödünç verilmiş kitaplar',
                                image = lent_books_icon,
                                compound = 'top')
        lent_books.pack(side = 'top', ipadx = 3, ipady = 1)

        category = ttk.Combobox(values = ['Çocuk', 'Dinî', 'Hikâye', 'Roman', 'Şiir', 'Tarihî', 'Yetişkin'],
                                state = 'readonly')
        category.bind('<<ComboboxSelected>>', lambda x: tbh.filter_table_by_genre(category.get(), table_tree))
        category.pack(side = 'right', anchor = 'nw')
        ttk.Label(text = '   Filtre:   ').pack(side = 'right', anchor = 'nw')

        global table_tree
        table_tree = ttk.Treeview(columns = ('Tür', 'Numara', 'Kitap adı', 'Yazar veya Çeviren'), show = 'headings')
        table_tree.heading('Tür', text = 'Tür'); table_tree.heading('Numara', text = 'Numara'); table_tree.heading('Kitap adı', text = 'Kitap adı'); table_tree.heading('Yazar veya Çeviren', text = 'Yazar veya Çeviren')
        table_tree.column('Tür', anchor = 'center'); table_tree.column('Numara', anchor = 'center'); table_tree.column('Kitap adı', anchor = 'center'); table_tree.column('Yazar veya Çeviren', anchor = 'center')
        table_tree.bind('<Button-3>', self.pop_up)
        table_tree.pack(fill = 'both', expand = True)

    def pop_up(self, event):
        menu = tk.Menu(tearoff = 0)
        menu.add_command(label = 'Düzenle', command = lambda: bkh.edit_book_gui(table_tree))
        menu.add_command(label = 'Sil')
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