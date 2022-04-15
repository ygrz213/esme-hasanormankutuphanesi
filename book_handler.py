from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import database_handler as dbh

######## (Functions to insert a temporary text to entry)
def on_entry_click(entry, temporary_string):
    if entry.get() == temporary_string:
        entry.delete(0, "end")
        entry.insert(0, '')
def on_focusout(entry, temporary_string):
    if not entry.get():
        entry.insert(0, temporary_string)
########


class add_book_gui(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.wm_iconbitmap('icons/book.ico')
        self.title('Esme Hasan ve Orman Kütüphanesi')
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.focus()

        self.widgets()

    def widgets(self):
        genre_frame = tk.Frame(self)
        genre_frame.pack()
        ttk.Label(genre_frame, text = 'Tür:').pack(padx = (0, 5), side = 'left')
        genre = ttk.Combobox(genre_frame, state = 'readonly', values = ['Çocuk', 'Dinî', 'Hikâye', 'Roman', 'Şiir', 'Tarihî', 'Yetişkin'])
        genre.pack(side = 'left')

        add_button_style = ttk.Style(); add_button_style.configure('Bold.TButton', font = 'Helvetica 10 bold')        # Style to make button bold
        add_book = ttk.Button(self,
                              text = 'Ekle',
                              cursor = 'hand2',
                              style = "Bold.TButton",
                              command = lambda: None if add_book_gui.check_entries(genre.get(), book_name.get(), writer.get()) else [dbh.dbhandler.add_book(genre.get(), book_name.get(), writer.get()), self.destroy()])
        add_book.pack(pady = (5, 0), side = 'bottom')

        writer = ttk.Entry(self, justify = 'center')
        writer.insert(0, 'Yazarın veya çevirenin adı')
        writer.bind('<FocusIn>', lambda x: on_entry_click(writer, 'Yazarın veya çevirenin adı')); writer.bind('<FocusOut>', lambda x: on_focusout(writer, 'Yazarın veya çevirenin adı'))
        writer.pack(fill = 'x', side = 'bottom')

        book_name = ttk.Entry(self, justify = 'center')
        book_name.insert(0, 'Kitap adı')
        book_name.bind('<FocusIn>', lambda x: on_entry_click(book_name, 'Kitap adı')); book_name.bind('<FocusOut>', lambda x: on_focusout(book_name, 'Kitap adı'))
        book_name.pack(fill = 'x', side = 'bottom')

    def check_entries(genre, book_name, writer):
        empty_entries_list = []

        for empty_entries in set(['', 'Kitap adı', 'Yazarın veya çevirenin adı']) & set([genre, book_name, writer]):
            if empty_entries == '':
                empty_entries_list.append('Tür')
            else:
                empty_entries_list.append(empty_entries)

        if empty_entries_list:
            messagebox.showerror('HATA', 'Geçersiz veri/veriler: ' + ', '.join(empty_entries_list))
            return True