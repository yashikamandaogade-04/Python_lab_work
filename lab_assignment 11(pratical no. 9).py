"""
#lab assignement 1 
class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")
    def display_data(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)
class Manager(Employee):
    pass
managers = []
for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_data()
    managers.append(m)
print("\nManager Information")
for i in managers:
    print("\nManager Details")
    i.display_data()
"""
#lab assignement 2 
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
class Library:
    def __init__(self):
        self.books = []
    def add_book(self):
        book_id = int(input("Enter book ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully")
    def lend_book(self):
        book_id = int(input("Enter book ID to lend: "))
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                print("Book issued successfully")
                return
        print("Book not available")
    def return_book(self):
        book_id = int(input("Enter book ID to return: "))

        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print("Book returned successfully")
                return
    def display_books(self):
        for book in self.books:
            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Available:", book.available)
library = Library()
while True:
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. Lend Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        library.add_book()
    elif choice == 2:
        library.lend_book()
    elif choice == 3:
        library.return_book()
    elif choice == 4:
        library.display_books()
    elif choice == 5:
        break