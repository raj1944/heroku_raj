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
def autocomplete():
    args = request.args

    q = args.get('q', default="")
    limit = args.get('limit', default=5)
    offset = args.get('offset', default=0)

    query = "SELECT * from branches WHERE branch LIKE %s order by ifsc limit %s offset %s"
    parem = ("%%" + q + "%%", limit, offset)
    rows = connection.execute(query, parem)
    
    json_data = {}
    json_data['banks'] = []
    
    for x in rows:
        temp_data = {}
        for i in range(len(header)):
            temp_data[header[i]] = x[i]
        json_data['banks'].append(temp_data) 

    query = "SELECT COUNT(*) from branches WHERE branch LIKE %s"
    rows = connection.execute(query, ("%%" + q + "%%"))
    for x in rows:
        json_data['page_count'] = (x[0] + limit - 1) // limit   
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



