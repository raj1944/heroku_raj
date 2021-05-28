from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="test2", user = "postgres", password = "raj", host = "127.0.0.1", port = "5432")

# print("Opened database successfully")

# cur = conn.cursor()

# @app.route('/api/branches/autocomplete')
# def hello():
#     args = request.args
#     print(args['q'])
#     query = 'SELECT * from branches' 
#     print(query)  
#     cur.execute(query)
#     rows = cur.fetchall()
#     json_data = {}
#     json_data['banks'] = []
#     for x in rows:
#         print(x)
#         json_data['banks'].append(list(x))
#     print(json_data)
#     return json_data

@app.route('/')
def home:
    return "hello"

# if __name__ == '__main__':
#     app.run()