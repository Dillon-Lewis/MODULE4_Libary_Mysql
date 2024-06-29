from DB_connections import connect_db, Error

def get_user():
    conn = connect_db()

    if conn is not None:
        try:
            user_name = input("Please enter the name of the user you are searching for").title()

            cursor = conn.cursor()

            query = 'SELECT * FROM users WHERE user_name = %s;'

            cursor.execute(query, (user_name,))

            id, user_name, email, phone = cursor.fetchall()[0]
            print(f'{id}. Name: {user_name} Email: {email} Phone: {phone}')

        except Error as e:
            print*f"Error: {e}"

        finally:
            cursor.close()
            conn.close()




def get_user_list():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = 'SELECT * FROM users;'

            cursor.execute(query)

            for id, user_name, email, phone in cursor.fetchall():
                print(f'{id}. Name: {user_name} Email: {email} Phone: {phone}')
                
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()