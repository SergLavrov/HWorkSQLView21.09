# Создать таблицу User: id, , имя, фамилия, отчесвто, дата рождения, город, страна, e-mail.
# Дата может быть только больше 1900.
# Создать view таблицы:
# 1. Имя, фамилия, e-mail у которых возраст меньше 18
# 2. Выборка людей: имя, фамилия, город, страна, которые проживают либо в России, либо в Беларуси,
#     которые старше 18 и у которых указан e-mail/
# 3. Проверить, чтобы e-mail был задан корректно: наличие символа @

CREATE TABLE user
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL ,
    lastName VARCHAR(25) NOT NULL ,
    birthday YEAR NOT NULL CHECK (birthday > 1900),
    city VARCHAR(50) NOT NULL ,
    country VARCHAR(50) NOT NULL ,
    eMail VARCHAR(30) NULL
);

INSERT INTO user (name, lastName, birthday, city, country, eMail)
values
    ('Ivan', 'Ivanov', 1976, 'Minsk', 'Belarus', NULL),
    ('Petr', 'Petrov', 1980, 'Minsk', 'Belarus', 'petrov@tut.by'),
    ('Stefan', 'Sedun', 1985, 'Roma', 'Italy', 'sed@mail.ru'),
    ('Mark', 'Muratov', 1987, 'Piter', 'Russia', NULL),
    ('Vlad', 'Vilkov', 1979, 'Vitebsk', 'Belarus', NULL),
    ('Nazar', 'Samoilov', 2009, 'Erevan', 'Armenia', 'nazar@tut.by'),
    ('Zahar', 'Tartur', 2008, 'Piter', 'Russia', NULL),
    ('Alex', 'Numirov', 2010, 'Tbilisi', 'Gorgia', 'ivanivan@tut.by'),
    ('Asan', 'Lukin', 2014, 'Omsk', 'Russia', 'lukich@gmail.ru');

SELECT * FROM user;

CREATE VIEW view_user_birthday AS
SELECT birthday, name, lastName, eMail FROM user
WHERE birthday > 2005;

CREATE VIEW view_user_country_birthday_eMail AS
SELECT * FROM user
WHERE (country = 'Belarus' OR country = 'Russia') and (birthday < 2005) and (eMail is not NULL);

CREATE VIEW view_user_eMail AS
SELECT eMail FROM user
WHERE eMail LIKE '%@%';
