# Christopher Villarreal
# Module 7 - Assignment 2 - Movies Queries
# November 30, 2025
# Purpose: Connect to the movies database and run queries to display studio records, genre records,
#          short films, and directors in order.

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

try:
    # try/catch block for handling potential MySQL database errors

    db = mysql.connector.connect(**config) # connect to the movies database 

    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

    # Continue with the mission
    # Query 1: Select all fields from studio
    cursor = db.cursor()
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")

    studios = cursor.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


    # Query 2: Select all fields from genre
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")

    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))


    # Query 3: Movie names with runtime < 2 hours (120 minutes)
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

    short_films = cursor.fetchall()
    for film in short_films:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))


    # Query 4: Film names and directors, grouped by director
    print("\n-- DISPLAYING Director RECORDS in Order --")
    cursor.execute(" SELECT film_name, film_director FROM film ORDER BY film_director")

    films = cursor.fetchall()
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))

    cursor.close()


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