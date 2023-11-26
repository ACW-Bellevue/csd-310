import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1qaz!QAZ1qaz!QAZ",
    "database": "movies"
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

print("--- DISPLAYING Studio RECORDS ---")
cursor.execute("SELECT * FROM studio;")
studios = cursor.fetchall()
for studio_id, studio_name in studios:
    print()
    print(f"Studio ID: {studio_id}")
    print(f"Studio Name: {studio_name}")
print()

print("--- DISPLAYING Genre RECORDS ---")
cursor.execute("SELECT * FROM genre;")
genres = cursor.fetchall()
for genre_id, genre_name in genres:
    print()
    print(f"Genre ID: {genre_id}")
    print(f"Genre Name: {genre_name}")
print()

print("--- DISPLAYING Short Film RECORDS ---")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")
short_films = cursor.fetchall()
for film_name, film_runtime in short_films:
    print()
    print(f"Film Name: {film_name}")
    print(f"Runtime: {film_runtime}")
print()

print("--- DISPLAYING Director RECORDS in Order ---")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")
films_directors = cursor.fetchall()
for film_name, film_director in films_directors:
    print()
    print(f"Film Name: {film_name}")
    print(f"Director: {film_director}")
print()

cursor.close()
connection.close()