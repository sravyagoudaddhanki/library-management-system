# Project Report: Library Management System

## 1. Introduction
This project is a Library Management System developed in Python
as part of the Think Champ Internship (Python with Generative AI,
May 2026). It is a terminal-based application that allows a
librarian to manage books — adding, viewing, searching, issuing,
and returning them — while automatically saving all records to
text files so data is not lost between runs.

## 2. Objective
The objective of this project is to build a menu-driven Python
program that can add new books, display all available books,
search books by title or author, issue books to users, accept
returned books, and store all library data persistently using
file handling.

## 3. Tools and Technologies Used
- Language: Python 3
- Concepts used: file handling, functions, loops, conditional
  statements, dictionaries, lists
- Storage: Plain text files (books.txt, issued_books.txt)
- Platform: GitHub Codespaces (VS Code in browser)

## 4. System Design
The program is divided into separate functions, each responsible
for one task:
- load_books() / save_books() — read and write book data
- load_issued() / save_issued() — read and write issued book data
- add_book() — adds a new book to the library
- view_books() — displays all books and their status
- search_book() — finds books by title or author
- issue_book() — marks a book as issued to a user
- return_book() — marks a book as available again
- main() — displays the menu in a loop and calls the right function

Each book is stored as one line in books.txt in the format:
title,author,status

## 5. Working
When the program starts, it loads existing book and issue records
from the text files into memory. It then displays a menu with six
options. Based on the user's choice, the corresponding function
runs. After every change (adding, issuing, or returning a book),
the updated data is immediately saved back to the text files so
the information is never lost, even if the program closes.

## 6. Testing
The following test cases were carried out and passed successfully:
1. Adding a new book — confirmed it appears in View Books
2. Viewing books — confirmed correct title, author, and status
3. Searching by title and author — confirmed correct matches
4. Issuing a book — confirmed status changes to "issued"
5. Returning a book — confirmed status changes back to "available"
6. Exiting the program — confirmed clean exit with goodbye message

## 7. Conclusion
The Library Management System successfully meets all mandatory
requirements of the project. It demonstrates the use of Python
fundamentals such as functions, loops, conditionals, and file
handling to build a working, persistent terminal application.

## 8. Author
Think Champ Internship - Python with Generative AI (May 2026)
