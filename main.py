from book_add import add_book
from book_get import get_book, get_encyclopedia
from user_add import add_user
from user_get import get_user, get_user_list
from rent_book import rent_book
from return_book import return_book

def main():
    while True:
        main_menu = input('''
Welcome to Springfield Library, located in beautiful Springfield, Oregon!
How may I help you today:

1. Book Encyclopedia
2. Springfield Book Club
4. Back to society
    ''')
        if main_menu == '1':
            book_encyclopedia()              
        elif main_menu == "2":
            Book_club()               
        elif main_menu == '4':
            print("Thank you for stopping by!")
            break
        else:
            print("Don't pull a Homer and please enter a valid selection.")
            continue


def book_encyclopedia():
    while True:
        book_menu = input('''
Welcome to the Book Encyclopedia, what would you like to do:

1. Add a new book
2. Rent a book
3. Return a book
4. Search the Encyclopedia 
5. Display the Encyclopedia
6. Back to main menu
    ''')
        if book_menu == '1':
            add_book()
        elif book_menu == '2':
            rent_book()
        elif book_menu == '3': 
            return_book()
        elif book_menu == '4':
            get_book()
        elif book_menu == '5':
            get_encyclopedia()
        elif book_menu == '6':
            return main()
        else:
            print("Don't pull a Homer and please enter a valid selection")
            continue


def Book_club():
    while True: 
        club_menu = input('''
Welcome to the Springfield Library Book Club! How can I help you friend:

1. Become a member
2. Search for a member
3. Display full member list
4. Back to main menu                         
    ''')
        if club_menu == '1':
            add_user()
        elif club_menu == '2':
            get_user()
        elif club_menu == '3': 
            get_user_list()
        elif club_menu == '4':
            return main()
        else:
            print("Don't pull a Homer and please enter a valid selection")
            continue


main()