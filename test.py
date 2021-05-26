from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="test2", user = "postgres", password = "raj", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

cur = conn.cursor()

@app.route('/api/branches/autocomplete')
def hello():
    cur.execute("SELECT * from banks where id <=10")
    rows = cur.fetchall()
    json_data = {}
    json_data['banks'] = []
    for x in rows:
        data = {}
        data['name'] = x[0]
        data['id'] = x[1]
        json_data['banks'].append(data)
    return json_data


if __name__ == '__main__':
    app.run()