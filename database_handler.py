import sqlite3 as sql

class book_db():
    def __init__(self):
        self.database = sql.connect('books.db')
        self.cursor = self.database.cursor()
        for genre in ['Çocuk', 'Dinî', 'Hikâye', 'Roman', 'Şiir', 'Tarihî', 'Yetişkin']:
            self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {genre} (Tür, Numara, Ad, Yazar veya Çeviren)''')

    def add_book(self, genre, book_name, writer):
        self.cursor.execute(f'''INSERT INTO '{genre}' VALUES ('{genre}', '{self.get_last_booknumber(genre) + 1}', "{book_name}", "{writer}")''')
        self.database.commit()

    def delete_book(self, genre, book_name):
        self.cursor.execute(f'''DELETE FROM '{genre}' WHERE Ad = "{book_name}" ''')
        self.database.commit()

    def edit_book(self, orig_genre, genre, orig_book_name, book_name, writer):
        if orig_genre != genre:        # If genre is changed
            self.add_book(genre, book_name, writer)
            self.delete_book(orig_genre, orig_book_name)
        else:
            self.cursor.execute(f'''UPDATE {orig_genre} SET Tür = '{genre}', Ad = "{book_name}", Yazar = "{writer}" WHERE Ad = "{orig_book_name}" ''')
        self.database.commit()

    def filter_category(self, category):
        return self.cursor.execute(f'''SELECT * FROM '{category}' ''').fetchall()

    def get_last_booknumber(self, genre):
        self.cursor.execute(f'''SELECT max(ROWID) FROM '{genre}' ''')
        result = self.cursor.fetchall()[0][0]

        if result is None:
            return 0
        return result

dbhandler = book_db()