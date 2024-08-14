
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__is_available

    def set_availability(self, status):
        self.__is_available = status

    def display_info(self):
        availability = "Available" if self.__is_available else "Borrowed"
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Genre: {self.__genre}")
        print(f"Publication Date: {self.__publication_date}")
        print(f"Status: {availability}")


    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        publication_date = input("Enter book publication date: ")
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
        print("Book added successfully.")


    def return_book(self):
        title = input("Enter the title of the book to return: ")
        for book in self.books:
            if book.get_title() == title and not book.is_available():
                book.set_availability(True)
                user_id = input("Enter your user ID: ")
                user = self.find_user(user_id)
                if user:
                    user.return_book(title)
                    print(f"You have returned '{title}'.")
                    self.check_reservations(title)
                return
        print("Book not found.")


    def search_book(self):
        title = input("What is the title of the book?: ")
        for book in self.books:
            if book.get_title() == title:
                book.display_info()
                return
        print("Book not found.")

    def display_all_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            book.display_info()


class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_library_id(self):
        return self.__library_id

    def get_name(self):
        return self.__name

    def borrow_book(self, book_title, due_date):
        self.__borrowed_books.append({"title": book_title, "due_date": due_date})

    def return_book(self, book_title):
        for book in self.__borrowed_books:
            if book["title"] == book_title:
                self.__borrowed_books.remove(book)
                return

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Library ID: {self.__library_id}")
        print("Borrowed Books:")


    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter user library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print("User added successfully.")

    def view_user_details(self):
        library_id = input("Enter user library ID: ")
        for user in self.users:
            if user.get_library_id() == library_id:
                user.display_info()
                return
        print("User not found.")

    def display_all_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            user.display_info()

    def find_user(self, library_id):
        for user in self.users:
            if user.get_library_id() == library_id:
                return user
        print("User not found.")
        return None

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Biography: {self.__biography}")



    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter author biography: ")
        new_author = Author(name, biography)
        self.authors.append(new_author)
        print("Author added successfully.")

    def view_author_details(self):
        name = input("Enter author name: ")
        for author in self.authors:
            if author.get_name() == name:
                author.display_info()
                return
        print("Author not found.")

    def display_all_authors(self):
        if not self.authors:
            print("No authors available.")
        for author in self.authors:
            author.display_info()

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.reservations = []


    def main_menu(self):
        while True:
            commands = (''' 
        Welcome to the Library Management System!

        Main Menu:
        1. Book Operations
        2. User Operations
        3. Author Operations
        4. Quit
                  
        ''')
        
            if commands == "1":
                self.book_operations()
            elif commands == "2":
                self.user_operations()
            elif commands == "3":
                self.author_operations()
            elif commands == "4":
                print("Exiting program")
                break
            else:
                print("Invalid entry, please try again.")


    def book_operations(self):
            while True:
                print("\nBook Operations:")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                print("6. Back to Main Menu")
                choice = input("Enter your choice: ")

                if choice == '1':
                    self.add_book()
                elif choice == '2':
                    self.borrow_book()
                elif choice == '3':
                    self.return_book()
                elif choice == '4':
                    self.search_book()
                elif choice == '5':
                    self.display_all_books()
                elif choice == '6':
                    break
                else:
                    print("Invalid entry, please try again.")


    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid entry, please try again.")


    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid entry, please try again.")
                
Library.main_menu()   




