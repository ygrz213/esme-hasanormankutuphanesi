import tkinter as tk
import tkinter.ttk as ttk
import database_handler as dbh
from ttkthemes import ThemedTk

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

        genre_frame = tk.Frame(self)
        genre_frame.pack()
        ttk.Label(genre_frame, text = 'Tür:').pack(padx = (0, 5), side = 'left')
        self.genre = ttk.Combobox(genre_frame, state = 'readonly', values = ['Hikâye', 'Roman'])
        self.genre.pack(side = 'left')

        add_button_style = ttk.Style(); add_button_style.configure('Bold.TButton', font = 'Helvetica 10 bold')        # Style to make button bold
        self.add_book = ttk.Button(self, text = 'Ekle', cursor = 'hand2', style = "Bold.TButton", command = lambda: [dbh.dbhandler.add_book(self.genre.get(), self.book_name.get(), self.writer.get()), self.destroy()])
        self.add_book.pack(pady = (5, 0), side = 'bottom')

        self.writer = ttk.Entry(self, justify = 'center')
        self.writer.insert(0, 'Yazarın veya çevirenin adı')
        self.writer.bind('<FocusIn>', lambda x: on_entry_click(self.writer, 'Yazarın veya çevirenin adı')); self.writer.bind('<FocusOut>', lambda x: on_focusout(self.writer, 'Yazarın veya çevirenin adı'))
        self.writer.pack(fill = 'x', side = 'bottom')

        self.book_name = ttk.Entry(self, justify = 'center')
        self.book_name.insert(0, 'Kitap adı')
        self.book_name.bind('<FocusIn>', lambda x: on_entry_click(self.book_name, 'Kitap adı')); self.book_name.bind('<FocusOut>', lambda x: on_focusout(self.book_name, 'Kitap adı'))
        self.book_name.pack(fill = 'x', side = 'bottom')