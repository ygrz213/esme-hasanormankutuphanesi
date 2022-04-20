from tkinter import ttk
import tkinter as tk
import database_handler as dbh
    
def update_table(category, tree):
    tree.delete(*tree.get_children())
    for column in dbh.dbhandler.filter_category(category):
        tree.insert('', 'end', values = column)