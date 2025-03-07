# Data Modeling for Sparkify
## Background 
### Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In order to carry out the analytics a a Postgres database with tables (shown below) has been designed to optimize queries on song play analysis. In project creates a database schema called Sparkify and ETL pipeline for the analysis. 

`Note: Background is based on Udacity Data Engineering Nano degree Program`

## Prerequisites for running the program
The project is built in python 3.x, and PostgreSQL.
A default database named a default studentdb is required for the porgramme to start. 

## File Info
### Data Files:
#### Song_data
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```json
song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
```

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

#### Log_data
The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```
log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
```
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

```	
|    | artist   | auth      | firstName   | gender   |   itemInSession | lastName   |   length | level   | location                          | method   | page     |   registration |   sessionId | song         |   status |            ts | userAgent                                                                                                                  |   userId |
|----|----------|-----------|-------------|----------|-----------------|------------|----------|---------|-----------------------------------|----------|----------|----------------|-------------|--------------|----------|---------------|----------------------------------------------------------------------------------------------------------------------------|----------|
|  0 |          | Logged In | Walter      | M        |               0 | Frye       |  nan     | free    | San Francisco-Oakland-Hayward, CA | GET      | Home     |    1.54092e+12 |          38 |              |      200 | 1541105830796 | "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36" |       39 |
|  1 |          | Logged In | Kaylee      | F        |               0 | Summers    |  nan     | free    | Phoenix-Mesa-Scottsdale, AZ       | GET      | Home     |    1.54034e+12 |         139 |              |      200 | 1541106106796 | "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"            |        8 |
|  2 | Des'ree  | Logged In | Kaylee      | F        |               1 | Summers    |  246.308 | free    | Phoenix-Mesa-Scottsdale, AZ       | PUT      | NextSong |    1.54034e+12 |         139 | You Gotta Be |      200 | 1541106106796 | "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"            |        8 |
|  3 |          | Logged In | Kaylee      | F        |               2 | Summers    |  nan     | free    | Phoenix-Mesa-Scottsdale, AZ       | GET      | Upgrade  |    1.54034e+12 |         139 |              |      200 | 1541106132796 | "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"            |        8 |
|  4 | Mr Oizo  | Logged In | Kaylee      | F        |               3 | Summers    |  144.039 | free    | Phoenix-Mesa-Scottsdale, AZ       | PUT      | NextSong |    1.54034e+12 |         139 | Flat 55      |      200 | 1541106352796 | "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"            |        8 |

```
`Information taken from Udacity Nano degree Programme`

### SQL Scripts:
1. sql_quries: All the PostgreSQL statements for Creating, Dropping, Inserting, and Selection.

### Python Scripts:
1. Create_tables.py: The script will connect to the default database, then drop all the tables in Sparkify Database, and then create all the tables from scratch by executinh `sql_quires` file.

2. Etl.py: The script used for extrating data from log_data and song_data. The script will transform the data from the file and load it into the database created by `sql_quries` and `create_tables.py`

### Dashboard
This showcases some of the dashboard created based on the analysis conducted on the users subscriptio, avg listening time per artist, and user by state.

```
Note: graph for user by state has mutiple states per user

```
## Execution of the project
1. Execute in `terminal:` `python create_tables.py` . This will create the database and drop.
2. Execute in `terminal:` `python etl.py`. This will extract, transform, and finally load the data in the database.
2. Open Dashboard for testing queries in the ipython notebook.


## ERD for sparkify
![alt text](https://github.com/mindfultime/nd027/blob/master/Progres_DataModelling/ERD.PNG "Logo Sparkify ERD")

