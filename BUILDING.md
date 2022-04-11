## .EXE Oluşturma

**1-** `icons/`'taki bütün dosyaları `main.py` ile aynı klasöre getirin.


**2-** PyInstaller yüklü değilse: `pip install pyinstaller`


**3-**
```python
import sys
import os

if not hasattr(sys, "frozen"):
    datafile = os.path.join(os.path.dirname(__file__), "book.ico")
else:
    datafile = os.path.join(sys.prefix, "book.ico")
def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
```

satırlarını `main.py`'nin başına ekleyin.


**4-**
```python
(Tk_veya_Toplevel).wm_iconbitmap('icons/book.ico')
```

ve

```python
        global x_book*_icon; x_book*_icon = tk.PhotoImage(file = 'icons/z.png')        # x (add, search, lend) * (hiçbir şey veya s) z (plus, search, lend)
```

kısımlarını sırasıyla

```python
(Tk_veya_Toplevel).iconbitmap(default=resource_path(datafile))
```

```python
        if not hasattr(sys, "frozen"):
            datafilex = os.path.join(os.path.dirname(__file__), "z.png")        # datafilex değişkeninin adı birden fazla fotoğraf için değiştirilebilir
        else:
            datafilex = os.path.join(sys.prefix, "z.png")
        global x_book*_icon; x_book*_icon = tk.PhotoImage(file = resource_path(datafilex))
```

olarak değiştirin.


**5-** `py -m PyInstaller --onefile --noconsole --hidden-import ttkthemes --add-data "book.ico;." --add-data "plus.png;." --add-data "search.png;." --add-data "lend.png;." --icon=book.ico main.py` komutunu çalıştırın. .EXE `dist/` klasöründe olacaktır.