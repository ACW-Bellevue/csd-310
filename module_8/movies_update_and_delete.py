import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1qaz!QAZ1qaz!QAZ",
    database="movies"
)
cursor = db.cursor()

def show_films(cursor, title):
    print(title)
    
    query = """
    SELECT f.film_name, f.film_director, g.genre_name, s.studio_name
    FROM film f
    JOIN genre g ON f.genre_id = g.genre_id
    JOIN studio s ON f.studio_id = s.studio_id
    ORDER BY f.film_id;
    """
    cursor.execute(query)
    
    films = cursor.fetchall()
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre Name ID: {film[2]}") 
        print(f"Studio Name: {film[3]}")
        print("")

show_films(cursor, "-- DISPLAYING FILMS --")

insert_query = """
INSERT INTO film (film_name, film_director, film_releaseDate, film_runtime, genre_id, studio_id) 
VALUES (%s, %s, %s, %s, %s, %s);
"""

film_releaseDate = '2023'
film_runtime = '180'
genre_id_value = 2
studio_id_value = 3

cursor.execute(insert_query, ('Oppenheimer', 'Christopher Nolan', film_releaseDate, film_runtime, genre_id_value, studio_id_value))
db.commit()

show_films(cursor, "-- DISPLAYING FILMS AFTER INSERT --")

horror_genre_id = 1

update_query = """
UPDATE film
SET genre_id = %s
WHERE film_name = 'Alien';
"""

cursor.execute(update_query, (horror_genre_id,))
db.commit()

show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --")

delete_query = """
DELETE FROM film
WHERE film_name = %s;
"""

cursor.execute(delete_query, ('Gladiator',))
db.commit()

show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE --")

cursor.close()
db.close()
