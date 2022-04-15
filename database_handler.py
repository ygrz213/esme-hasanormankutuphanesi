import sqlite3 as sql

class book_db():
    def __init__(self):
        self.database = sql.connect('books.db')
        self.cursor = self.database.cursor()
        for genre in ['Çocuk', 'Dinî', 'Hikâye', 'Roman', 'Şiir', 'Tarihî', 'Yetişkin']:
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {genre} (Numara, Ad, Yazar veya Çeviren)''')

    def add_book(self, genre, book_name, writer):
        self.cursor.execute(f'''INSERT INTO '{genre}' VALUES ('{self.get_last_booknumber(genre) + 1}', "{book_name}", "{writer}")''')
        self.database.commit()

    def get_last_booknumber(self, genre):
        self.cursor.execute(f'''SELECT max(ROWID) FROM '{genre}' ''')
        result = self.cursor.fetchall()[0][0]

        if result is None:
            return 0
        return result

dbhandler = book_db()