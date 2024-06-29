-- Lets create the database

CREATE DATABASE Library_Management;

-- Now lets create our tables

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(75) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE,
    phone VARCHAR(14) NOT NULL
);

CREATE TABLE books(
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(150) NOT NULL,
	author VARCHAR(150) NOT NULL,
	availability VARCHAR(40) DEFAULT "available for rent"
);

CREATE TABLE borrowed_books(
	id INT AUTO_INCREMENT PRIMARY KEY,
	user_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

INSERT INTO users (user_name, email, phone)
VALUES ('Marge Simpson', 'MargeS@gmail.com', '789-456-1245'),
('Ned Flanders', 'LiveBreathGod@gmail.com', '456-124-8457'),
('Ralph Wiggum', 'ImInDanger4@yahoo.com', '455-125-5423'),
('Moe', 'DrinkatMoes@yahoo.com', '122-432-6783');

INSERT INTO books (title, author)
VALUES ('The Hobbit', 'J. R. R. Tolkien'),
('The Shining', 'Steven King'),
('The Catcher in the Rye', 'J.D. Salinger'),
('Florida Man', 'Mike Baron'),
('Into The Wild', 'Jon Krakauer');

SELECT * FROM users;
SELECT * FROM books;
