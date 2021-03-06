# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY,
start_time timestamp , 
user_id int references users(user_id), 
level varchar, 
song_id varchar NOT NULL references songs(song_id),  
artist_id varchar NOT NULL references artists(artist_id), 
session_id int , 
location varchar , 
user_agent varchar)
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY,
first_name varchar, 
last_name varchar, 
gender varchar, 
level varchar)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, 
title varchar NOT NULL, 
artist_id varchar, 
year int NOT NULL, 
duration numeric NOT NULL)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, 
name varchar NOT NULL, 
location varchar NOT NULL,
latitude double precision , 
longitude double precision )
""")


time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, 
hour int, 
day int, 
week int, 
month int, 
year int, 
weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, 
user_id, 
level, 
song_id ,  
artist_id , 
session_id , 
location , 
user_agent) VALUES (%s, %s, %s,%s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""INSERT INTO users VALUES (%s, %s, %s,%s, %s) ON CONFLICT (user_id) DO UPDATE SET level=excluded.level
""")

song_table_insert = ("""INSERT INTO songs VALUES (%s, %s, %s,%s, %s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists VALUES (%s, %s, %s,%s, %s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""INSERT INTO time VALUES (%s, %s, %s,%s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""select song_id , artists.artist_id from songs
join artists on songs.artist_id = artists.artist_id
where %s is not null 
and %s is not null
and %s is not null
""")
#Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]