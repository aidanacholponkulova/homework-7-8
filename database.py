import sqlite3


def create_table(connection):
    connection.execute(""" 
        CREATE TABLE IF NOT EXISTS books ( 
            name TEXT, 
            author TEXT, 
            publication_year INTEGER,
            genre TEXT, 
            number_of_pages INTEGER, 
            number_of_copies INTEGER 
        )
    """)
    connection.commit()


def insert_books(connection): 
    books = [
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 223, 5),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 4), 
        ("1984", "George Orwell", 1949, "Dystopia", 328, 6), 
        ("The Little Prince", "Antoine de Saint-Exupery", 1943, "Fantasy", 96, 3),
        ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 432, 2), 
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 5), 
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Novel", 671, 3), 
        ("War and Peace", "Leo Tolstoy", 1869, "Historical novel", 1225, 2), 
        ("The Alchemist", "Paulo Coelho", 1988, "Adventure", 208, 4), 
        ("Animal Farm", "George Orwell", 1945, "Satire", 112, 6)
    ]

    for book in books:
        connection.execute("""
            INSERT INTO books (
                name,
                author,
                publication_year,
                genre,
                number_of_pages,
                number_of_copies
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, book)

    connection.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("books.db")

    create_table(connection)
    insert_books(connection)

    print("Table created successfully!")
    print("10 books added successfully!")

    connection.close()
