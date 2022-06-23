# Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals:

The purpose of this database is to allow all users in Sparkify to be available to query in a simple way whatever information or KPI of the company they want to know.
The analytics goals could be to get information about what are the most frequent time frames, or what users, artists or songs are most listened, etc, etc.

# How to run the Python scripts:

The python scrips could be run open the terminal and running: python file.py

# An explanation of the files in the repository:

In the repository we have two folder of files (all files in JSON formats):
Song files: In this folder we can found information related the songs and their belong artists. 

Log files: In this folder we can found information related the songs played with their timestamp and users who have listented to.


# State and justify your database schema design and ETL pipeline:

For this case, we have build an star schema, with the fact table (songplay table) in which are present all the songs played by the users and the fact tables: users, artists, time and songs.