"""
Workflow:
    kindle--->book

Object:
    kindle
    book
    format:
        PDF
        MOBI
        EPUD

Case:
    download
    upload
    delete 
"""


class Kindle:
    def __init__(self):
        self.books = dict()
        self.reader = Reader()

    def readBook(self, book_name):
        if book_name not in self.books:
            print('book not exist')
            return
        book = self.books[book_name]
        reader = self.reader.creat_reader(book)
        reader.read(book)

    def download(self, book):
        pass

    def upload(self, book_name,book_format):
        if book_name in self.books:
            print('book already exist')
            return

        new_book = Book(book_name, book_format)
        self.books[book_name] = new_book
        

    def delete(self, book_name):
        if book_name in self.books:
            print('book already exist')
            return
        del self.books[book_name]

class Book:
    def __init__(self, n, f):
        self.name = n
        self.format = f

class Reader:
    def creat_reader(self, book):
        if book.format == 'EPUB':
            return  EPUDReader()
        elif book.format == 'PDF':
            return  PDFReader() 
        elif book.format == 'MOBI':
            return  MOBIReader() 

class EPUDReader(Reader):
    def read(self,book):
        print('Using EPUB reader, book content is: ', book.name)

class PDFReader(Reader):
    def read(self,book):
        print('Using PDF reader, book content is: ', book.name)
    
class MOBIReader(Reader):
    def read(self,book):
        print('Using PDF reader, book content is: ', book.name)


kindle = Kindle()
kindle.upload('EPUBBook', 'EPUB')
kindle.readBook('EPUBBook')
kindle.readBook('PDFBook')
