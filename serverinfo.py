$ sqlite3 server_information.db 
$ sqlite> .mode csv server
$ sqlite> .import server.csv server_information


$ virtualenv rest-api 
$ source rest-api/bin/activate 
$ mkdir ~/rest-app $ cd ~/rest-app

$ pip install flask 
$ pip install flask-restful

from flask import Flask, request 
from flask_restful import Resource, Api 
from sqlalchemy import create_engine 
from json import dumps  

e = create_engine('sqlite:///server_information.db')  
app = Flask(__name__) 
api = Api(app)  
class processador(Resource):     
def get(self):         
#Connect to databse         
conn = e.connect()
query = conn.execute("select distinct processador from server_information")         
return {'processador': [i[0] for i in query.cursor.fetchall()]}  
class processo(Resource):     
def get(self):         
#Connect to databse         
conn = e.connect()
query = conn.execute("select distinct processo from server_information")         
return {'processo': [i[0] for i in query.cursor.fetchall()]}

class sessao(Resource):     
def get(self):         
#Connect to databse         
conn = e.connect()
query = conn.execute("select distinct sessao from server_information")         
return {'sessao': [i[0] for i in query.cursor.fetchall()]}
class nome_sistema(Resource):     
def get(self):         
#Connect to databse         
conn = e.connect()
query = conn.execute("select distinct nome_sistema from server_information")         
return {'nome_sistema': [i[0] for i in query.cursor.fetchall()]}
class versao_sistema(Resource):     
def get(self):         
#Connect to databse         
conn = e.connect()
query = conn.execute("select distinct versa_sistema from server_information")         
return {'versao_sistema': [i[0] for i in query.cursor.fetchall()]}
return result

 api.add_resource(Departmental_Salary, '/dept/<string:department_name>') 
api.add_resource(Departments_Meta, '/departments')  if __name__ == '__main__':      app.run()

$ python app.py 

