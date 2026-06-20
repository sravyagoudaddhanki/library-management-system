import os

BOOKS_FILE = "books.txt"
ISSUED_FILE = "issued_books.txt"

def load_books():
    books = []
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        title, author, status = parts
                        books.append({"title": title, "author": author, "status": status})
    return books

def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        for b in books:
            f.write(f"{b['title']},{b['author']},{b['status']}\n")

def load_issued():
    issued = []
    if os.path.exists(ISSUED_FILE):
        with open(ISSUED_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 2:
                        title, user = parts
                        issued.append({"title": title, "user": user})
    return issued


def save_issued(issued):
    with open(ISSUED_FILE, "w") as f:
        for i in issued:
            f.write(f"{i['title']},{i['user']}\n")

def add_book(books):
    title = input("Enter Book Name: ").strip()
    author = input("Enter Author Name: ").strip()
    books.append({"title": title, "author": author, "status": "available"})
    save_books(books)
    print("Book Added Successfully!")
def view_books(books):
    if not books:
        print("No books available in the library.")
        return
    print("Available Books:")
    for idx, b in enumerate(books, start=1):
        print(f"{idx}. {b['title']} by {b['author']} - [{b['status']}]")
def search_book(books):
    keyword = input("Enter Title or Author to search: ").strip().lower()
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]
    if results:
        print("Search Results:")
        for idx, b in enumerate(results, start=1):
            print(f"{idx}. {b['title']} by {b['author']} - [{b['status']}]")
    else:
        print("No matching books found.")
