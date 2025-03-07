# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                            (songplay_id serial PRIMARY KEY,
                            start_time bigint NOT NULL,
                            user_id int ,
                            level varchar NOT NULL,
                            song_id varchar ,
                            artist_id varchar ,
                            session_id int NOT NULL,
                            location varchar NOT NULL,
                            state varchar,
                            user_agent varchar );""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
                        (user_id varchar PRIMARY KEY,
                        first_name varchar NOT NULL,
                        last_name varchar ,
                        gender char NOT NULL,
                        level varchar NOT NULL);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS 
                        songs(song_id varchar PRIMARY KEY,
                        title varchar NOT NULL,
                        artist_id varchar NOT NULL,
                        year int,
                        duration float);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                    (artist_id varchar PRIMARY KEY,
                    name varchar NOT NULL,
                    location varchar NOT NULL,
                    latitude real,
                    longitude real);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
                        (start_time timestamp ,
                        hour int NOT NULL,
                        day int NOT NULL,
                        week int NOT NULL,
                        month int NOT NULL, 
                        year int NOT NULL,
                        weekday int NOT NULL);""")

# INSERT RECORDS
#reference: https://www.postgresql.org/docs/9.5/sql-insert.html#SQL-ON-CONFLICT

songplay_table_insert = ("""INSERT INTO songplays
                            (start_time, user_id, level, song_id, artist_id,session_id, location, user_agent) 
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s);""")
user_table_insert = ("""INSERT INTO users(user_id, first_name, last_name, gender, level)
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT(user_id) DO UPDATE
                            SET first_name = excluded.first_name,
                                last_name = excluded.last_name,
                                gender = excluded.gender,
                                level = excluded.level;""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration)
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT (song_id) DO UPDATE
                            SET title = excluded.title,
                                artist_id = excluded.artist_id,
                                year = excluded.year,
                                duration = excluded.duration;""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude)
                        VALUES(%s,%s,%s,%s,%s)
                        ON CONFLICT (artist_id) DO UPDATE
                            SET name = excluded.name,
                                location = excluded.location,
                                latitude = excluded.latitude,
                                longitude = excluded.longitude;""")


time_table_insert = ("""INSERT INTO time(start_time, hour, day, week, month, year, weekday)
                        VALUES(%s,%s,%s,%s,%s,%s,%s);""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id 
                FROM songs s
                JOIN artists a ON s.artist_id = a.artist_id 
                WHERE s.title = %s AND a.name = %s AND s.duration = %s;""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


# DASHBOARD QUERIES 
#reference:https://w3resource.com/PostgreSQL/split_part-function.php

user_location= """SELECT count(user_id),split_part(location, ',', 2) state 
                    FROM songplays 
                    GROUP BY location
                    ORDER BY count DESC;"""


avg_song_duration_per_artist="""SELECT a.name artist_name,avg(duration) avg_duration 
                    FROM songs s
                    JOIN artists a
                    ON a.artist_id = s.artist_id
                    GROUP BY (name) 
                    ORDER BY avg_duration DESC"""

users_subscription ="""SELECT level subscription_type, count(user_id) number_of_users FROM songplays GROUP BY level"""

