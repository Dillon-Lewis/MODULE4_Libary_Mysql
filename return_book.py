from DB_connections import connect_db, Error

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            title = input("Please enter the title of the book you are trying to return").title()

            cursor = conn.cursor()

            query = conn.cursor()

            query = 'SELECT * FROM books WHERE title = %s'

            cursor.execute(query, (title, ))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author} is currently {availability}.')

            if availability == "out on rental":

                change_availability = "available for rent"

                availability_update = (change_availability, title)

                query2 = conn.cursor()

                query2 = 'UPDATE books SET availability = %s WHERE title = %s;'

                cursor.execute(query2, availability_update)
                conn.commit()
                print(f"Thank you for returning {title}, we hope you enjoyed it!")

            elif availability == "available for rent":
                print("You might want to see where you got that book from because that isn't ours.")
        except IndexError:
            print("Please enter a valid title you would like to rent and try again.")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
