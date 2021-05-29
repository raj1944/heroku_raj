
from sqlalchemy import *
from config import host, port, database, user, password
import psycopg2
from flask import Flask, request
app = Flask(__name__)
conn_str = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str)
connection = engine.connect()
# conn = psycopg2.connect(database="test", user = "princepansheriya", password = "prince", host = "127.0.0.1", port = "5432")

print ("Opened database successfully")
# cur = connection.cursor()
@app.route('/api/branches/autocomplete')
def hello():
    # return 'prince'
    args = request.args
    print(args['q'])
    # query = 'SELECT * from branches where branch="RTGS-HO"'
    s = ""
    s += "SELECT * from branches "
    s += "WHERE"
    s += "("
    s += " branch = '" + args['q'] + "'"
    s += ")"
    print(s)  
    rows = connection.execute(s)
    # rows = connection.fetchall()
    json_data = {}
    json_data['banks'] = []
    for x in rows:
        # print(x)
        json_data['banks'].append(list(x))
    print(json_data)
    return json_data



