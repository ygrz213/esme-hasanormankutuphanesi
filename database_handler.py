import sqlite3 as sql

class edit_db():
    def __init__(self):
        self.database = sql.connect('books.db')
        self.cursor = self.database.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Kitaplar (Tür, Numara, Ad, Yazar veya Çeviren)''')

    def add_book(self, genre, book_name, writer):
        self.cursor.execute(f'''INSERT INTO Kitaplar VALUES ('{genre}', '{self.get_last_booknumber() + 1}', '{book_name}', '{writer}')''')
        self.database.commit()

    def get_last_booknumber(self):
        self.cursor.execute('''SELECT max(ROWID) FROM Kitaplar''')
        result = self.cursor.fetchall()[0][0]
        if result is None:
            return 0
        else:
            return result

dbhandler = edit_db()