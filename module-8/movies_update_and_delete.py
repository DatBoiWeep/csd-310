# Christopher Villarreal
# Module 8 - Assignment 2 - Movies Queries
# November 30, 2025
# Purpose: Perform insert, update, and delete operations on film records table in the movies database.

# import statements
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

# database config object
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}

def show_films(cursor, title):

    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:
    # try/catch block for handling potential MySQL database errors 

    db = mysql.connector.connect(**config) # connect to the movies database 

    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    # Inserts 'Back to the Future' into film table
    new_film_query = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Back to the Future', '1985', '116', 'Robert Zemeckis', 3, 2)"
    cursor.execute(new_film_query)

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Updates 'Alien' to genre_id 1 (Horror)
    update_film_query = "UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'"
    cursor.execute(update_film_query)

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

    # Deletes 'Gladiator' from film table
    delete_film_query = "DELETE FROM film WHERE film_name = 'Gladiator'"
    cursor.execute(delete_film_query)

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


except mysql.connector.Error as err:
    # on error code

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # close the connection to MySQL

    db.close()