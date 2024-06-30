from DB_connections import connect_db, Error

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("Lets get that new book in our encyclopedia!\nWhat is the title of the book you would like to add: \n").title()
            author = input("Who is the author of the book: \n").title()

            new_member = (title, author)

            query = 'INSERT INTO books (title, author) VALUES (%s, %s);'

            cursor.execute(query, new_member)
            conn.commit()
            print(f"{title} by {author} has successfully been added to the encyclopedia!")

        except IndexError:
            print("Please enter a valid response and try again.")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()