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
