import sqlite3 
import json

#Conexion sqlite 

conexion = sqlite3.connect('proyectouc.sqlite')
cursor = conexion.cursor()

#Verificamos si la tabla de base de datos existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Project_UC (
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,   
        Gender TEXT,
        PlanDeSalud TEXT,
        Phone INTEGER
    )
''')
                

#Carga de datos desde el archivo JSON

with open('MOCK_DATA.json', 'r') as archivo:
    datos_json = json.load(archivo)
    
#Insertar datos de registro en tablas

for i, dato in enumerate(datos_json):
    if i < 500:
        cursor.execute(''' 
            INSERT INTO Project_UC (FirstName, LastName, Email, Gender, PlanDeSalud, Phone)
            VALUES (?,?,?,?,?,?)
        ''', (dato['first_name'], dato['last_name'], dato['email'], dato['gender'], dato['Plan de Salud'], dato['phone']))
    else:
        break  
    
# Realiza un commit para guardar los cambios en la base de datos
conexion.commit()

# Cierra la conexión a la base de datos cuando hayas terminado
conexion.close()

