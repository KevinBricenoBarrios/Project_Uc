from fastapi import FastAPI, HTTPException
import sqlite3


app = FastAPI()

# Función para conectar a la base de datos
def conexiondb():
    return sqlite3.connect('proyectouc.sqlite')

# Ruta para obtener información de un paciente por email
@app.get("/api/paciente/{email}")
def get_paciente_by_email(email: str):
    try:
        conexion = conexiondb()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT * FROM Project_UC WHERE Email = ?", (email,))
        paciente = cursor.fetchone()
        conexion.close()

        if paciente:
            return {
                "FirstName": paciente[0],
                "LastName": paciente[1],
                "Email": paciente[2],
                "Gender": paciente[3],
                "PlanDeSalud": paciente[4],
                "Phone": paciente[5]
            }
        else:
            raise HTTPException(status_code=404, detail="Paciente no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
