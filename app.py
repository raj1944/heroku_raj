from sqlalchemy import *
from config import host, port, database, user, password
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

conn_str = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(conn_str)

connection = engine.connect()

header = ["ifsc", "bank_id", "branch", "address", "city", "district", "state"]

@app.route('/')
def hello():
    return "RAJ"

@app.route('/api/branches/autocomplete')
def autocomplete(limit = 5, offset = 0):
    args = request.args
    query = "SELECT * from branches WHERE branch LIKE %s order by ifsc limit %s offset %s"
    parem = ("%%" + args.get('q', default="") + "%%", args.get('limit', default=5), args.get('offset', default=0))
    rows = connection.execute(query, parem)
    
    json_data = {}
    json_data['banks'] = []
    
    for x in rows:
        temp_data = {}
        for i in range(len(header)):
            temp_data[header[i]] = x[i]
        json_data['banks'].append(temp_data) 

    return json_data

@app.route('/api/branches')
def branches():
    args = request.args
    
    query = "SELECT * from branches WHERE branch ILIKE %s OR address ILIKE %s OR state ILIKE %s OR district ILIKE %s OR city ILIKE %s order by ifsc limit %s offset %s"
    parem = ("%%" + args['q'] + "%%", "%%" + args['q'] + "%%", "%%" + args['q'] + "%%", "%%" + args['q'] + "%%", "%%" + args['q'] + "%%", args.get('limit', default=5), args.get('offset', default=0))
    rows = connection.execute(query, parem)
    
    json_data = {}
    json_data['banks'] = []
    
    for x in rows:
        temp_data = {}
        for i in range(len(header)):
            temp_data[header[i]] = x[i]
        json_data['banks'].append(temp_data) 
    
    return json_data



