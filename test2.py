import psycopg2
import csv


conn = psycopg2.connect(database="test2", user = "postgres", password = "raj", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()


with open('data.csv', 'r') as f:
    next(f) # Skip the header row.
    cur.copy_from(f, 'branches', sep=',')
conn.commit()