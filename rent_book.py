from DB_connections import connect_db, Error

def rent_book():
    conn = connect_db()
    if conn is not None:
        try:
            title = input("Please enter the title of the book you are trying to rent").title()

            cursor = conn.cursor()

            query = conn.cursor()

            query = 'SELECT * FROM books WHERE title = %s'

            cursor.execute(query, (title, ))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author} is currently {availability}.')
            
            if availability == "available for rent":
                
                change_to_rented = "out on rental"
                
                availability_update = (change_to_rented, title)

                query2 = conn.cursor()

                query2 = 'UPDATE books SET availability = %s WHERE title = %s;'

                cursor.execute(query2, availability_update)
                conn.commit()
                print(f"Here you go, enjoy reading {title} and bring it back when you are done")

            elif availability == "out on rental":
                print(f"We are sorry, but {title} is currently out for rent. Check back later and we will have it back in stock")
        except IndexError:
            print("Please enter a valid title you would like to rent and try again.")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()



