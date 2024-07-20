# Question 2

# Task 1

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    book = (title, author)
    
    if book not in library:
        library.append(book)
        print(f"The book '{book[0]}' by '{book[1]}' has been added to the library.")
    else:
        print(f"The book '{book[0]}' by '{book[1]}' is already in the library.")
    return library

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add a new book
library = add_book(library)

# Print the updated library
print(library)