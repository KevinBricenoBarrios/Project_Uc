import sqlite3 
import json


#Carga de datos desde el archivo JSON

with open('MOCK_DATA.json') as file:
    data = json.load(file)
    
    
#Conexion sqlite 

conexion = sqlite3.connect('proyectouc.sqlite')
cursorBD = conexion.cursor()

#Verificamos si la tabla de base de datos existe
cursorBD.execute(''' CREATE TABLE PROJECT(ID INTEGER PRIMARY KEY AUTOINCREMENT,FIRST_NAME TEXT,LAST NAME TEXT,EMAIL TEXT,GENDER TEXT,PLAN DE SALUD TEXT,PHONE INTEGER )''')