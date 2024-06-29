from DB_connections import connect_db, Error

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input('So excited to hear you want to be become a member of our awesome libary!\n Pleas enter your name:  ').title()
            email = input("Please enter your email: ")
            phone = input("What is your phone number: ")

            new_member = (name, email, phone)

            query = 'INSERT INTO users (user_name, email, phone) VALUES (%s, %s, %s)'

            cursor.execute(query, new_member)
            conn.commit()
            print(f"Welcome {name} to the Springfield Family!")
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

                