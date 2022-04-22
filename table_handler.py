from tkinter import ttk
import tkinter as tk
import database_handler as dbh
    
def filter_table_by_genre(genre, tree):
    tree.delete(*tree.get_children())
    for column in dbh.dbhandler.filter_category(genre):
        tree.insert('', 'end', values = column)

def filter_table(genre, number, book_name, writer, tree):
    query = f'''SELECT * FROM '''

    if not genre:
        query += '''Çocuk
SELECT * FROM Dinî
SELECT * FROM Hikâye
SELECT * FROM Roman
SELECT * FROM Şiir
SELECT * FROM Tarihî
SELECT * FROM Yetişkin
'''
    else:
        query += f'{genre}\n'

    if number != 'Numara':        # If number is changed
        query = query.replace('\n', f''' WHERE Numara = {number}\n''')        # Change end of line as "WHERE Numara = {number}"
    if book_name != 'Kitap adı':
        if f''' WHERE Numara = {number}\n''' in query:        # If number is changed
            query = query.replace('\n', f''' AND\n''')        # Add "and" operator
            query = query.replace('\n', f''' Ad = '{book_name}'\n''')        # Change end of line as "Ad = '{book_name}'"
        else:        # If number is not
            query = query.replace('\n', f''' WHERE Ad = '{book_name}'\n''')        # Add "Ad = '{book_name}'" with WHERE statement
    if writer != 'Yazarın veya çevirenin adı':
        if f''' Ad = '{book_name}'\n''' in query or f''' WHERE Numara = {number}\n''' in query:
            query = query.replace('\n', f''' AND\n''')
            query = query.replace('\n', f''' "Yazar veya Çeviren" = '{writer}'\n''')
        else:
            query = query.replace('\n', f''' WHERE "Yazar veya Çeviren" = '{writer}'\n''')

    unioned_queries = []
    for single_query in query[:-2].splitlines(True)[:-1]:        # query[:-2].splitlines(True)[:-1]  query[:-2] -->query without last "\n"
                                                                 # .splitlines(True) --> To be able to detect \n character inside loop])
                                                                 # [:-1] --> Without the last line, sqlite would raise a syntax error when placing "UNION" to the last line
        unioned_queries.append(single_query.replace('\n', f''' UNION\n'''))
    unioned_queries.append(query.splitlines()[-1])        # Add union-free line, too

    query = ''.join(unioned_queries)        # Last form of query

    result = dbh.dbhandler.cursor.execute(query).fetchall()
    tree.delete(*tree.get_children())
    for column in result:
        tree.insert('', 'end', values = column)