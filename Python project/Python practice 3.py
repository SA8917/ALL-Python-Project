#WELCOME TO LIBRARY MANAGEMENT SYSTEM

#All THE Functions:

import json

books = {}
members = {}

def save_books_to_file(): #Saving files function
    try:
        with open('Library.json', 'w') as storage:
            json.dump(books, storage)
    except Exception as e:
        print(f"An error occuerred while saving books: {e}")

def save_members_to_file(): #Saving files function
    try:
        with open('Library.json', 'w') as storage:
            json.dump(members, storage)
    except Exception as e:
        print(f"An error occuerred while saving members: {e}")

def load_books_from_file():  # Loading files function
    global books
    try:
        with open('Library.json', 'r') as storage:
            books = json.load(storage)
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        books = {}
    except Exception as e:
        print(f"An error occurred while loading books: {e}")
        books = {}

def load_members_from_file():  # Loading files function
    global members
    try:
        with open('Library.json', 'r') as storage:
            members = json.load(storage)
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        members = {}
    except Exception as e:
        print(f"An error occurred while loading members: {e}")
        members = {}

def add_book():
    while True:
        book_name = input("Enter the name of the book: ")
        if book_name in books:
            print("Book already exists.")
        else:
            author = input("Enter the author of the book: ")
            books[book_name] = author
            print("Book added successfully.")
            save_books_to_file()
            break

def remove_book():
    while True:
        book_name = input("Enter the name of the book: ")
        if book_name in books:
            del books[book_name]
            print("Book removed successfully.")
            save_books_to_file()
            break
        else:
            print("Book not found.")

def add_member():
    while True:
        member_name = input("Enter the name of the member: ")
        if member_name in members:
            print("Member already exists.")
        else:
            address = input("Enter the address of the member: ")
            members[member_name] = address
            print("Member added successfully.")
            save_members_to_file()
            break

def remove_member():
    while True: 
        member_name = input("Enter the name of the member: ")
        if member_name in members:
            del members[member_name]
            print("Member removed successfully.")
            save_members_to_file()
            break
        else:
            print("Member not found.")
            break

def display_books():
    for book_name, author in books.items():
        print(f"Book: {book_name}, Author: {author}")

def display_members():
    for member_name, address in members.items():
        print(f"Member: {member_name}, Address: {address}")
#Loading the files

load_books_from_file()
load_members_from_file()
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Member")
        print("4. Remove Member")
        print("5. Display Books")
        print("6. Display Members")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            add_member()
        elif choice == "4":
            remove_member()
        elif choice == "5":
            display_books()
        elif choice == "6":
            display_members()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
