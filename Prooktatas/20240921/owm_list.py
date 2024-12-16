class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.auther = author
        self.year = year

    def __str__(self):
        return f"{self.book_id}: {self.title} írta {self.author} - {self.year}"


class BookList(list):

    def append(self, book):
        if not isinstance(book, Book):
            raise TypeError('Csak Book tipusú objektumokkat lehet hozzáadni')
        if any(b.book_id == book.book_id for b in self):
            raise ValueError(f"a {book.book_id} azonoítójú könyv már szerepel")
        super().append(book)
        print(f'Köny hozzáadva: {book}')

    def remove(self, book_id):
        for book in self:
            if book.book_id == book_id:
                super().remove(book)
                print(f"A könyv eltávolítva: {book}")
                return
        raise ValueError(f"A {book_id} azonosítójú könyv nem található")

    def list_books(self):
        if not self:
            print("Nincs könyv a liistában")
        else:
            print('Könyvek listája: ')
            for book in self:
                print(book)

    def search(self, book_id):
        for book in self:
            if book.book_id == book_id:
                print(f'A könnyv megtalálva: {book}')
                return book
        raise ValueError(f"A {book_id} azaonsítójú könyv nem található ")

    def update(self, book_id, title=None, author=None, year=None):
        book = self.search(book_id)
        if title:
            book.title = title
        if author:
            book.auther = author
        if year:
            book.year = year
        print(f"A könyv sikeresen módosítva: {book}")


book_list = BookList()

book1 = Book("B001", "könyvnek a címe", "könyv szerzője", 2000)
book2 = Book("B002", "könyvnek a címe", "második szerzője", 2001)
