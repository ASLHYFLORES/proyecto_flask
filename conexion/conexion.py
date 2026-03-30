import mysql.connector

def obtener_conexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Deja vacío si no tienes clave en XAMPP
            database="desarrollo_web" # Asegúrate que este nombre sea igual al de tu DB
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None