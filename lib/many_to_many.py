class Author:

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self._title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set([contract.author for contract in self.contracts()]))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")
        if not isinstance(date, str):
            raise Exception("Date must be of type str")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be of type int")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date):
        
        return [contract for contract in cls.all if contract.date == date]
