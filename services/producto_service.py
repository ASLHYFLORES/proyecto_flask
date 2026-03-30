import mysql.connector

class ProductoService:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="", 
            database="desarrollo_web"
        )

    @staticmethod
    def listar_todos():
        try:
            conn = ProductoService.conectar()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos")
            datos = cursor.fetchall()
            conn.close()
            return datos
        except:
            return []

    @staticmethod
    def listar_facturas():
        try:
            conn = ProductoService.conectar()
            cursor = conn.cursor(dictionary=True)
            # Solo pedimos la tabla facturas
            cursor.execute("SELECT * FROM facturas")
            datos = cursor.fetchall()
            conn.close()
            return datos
        except Exception as e:
            print(f"Error en facturas: {e}")
            return []

    # --- NUEVA FUNCIÓN PARA AÑADIR PRODUCTOS ---
    @staticmethod
    def crear_producto(nombre, precio, stock):
        try:
            conn = ProductoService.conectar()
            cursor = conn.cursor()
            # La instrucción SQL para insertar en la base de datos
            query = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, precio, stock))
            conn.commit() # ¡Esto hace que se guarde de verdad!
            conn.close()
            return True
        except Exception as e:
            print(f"Error al añadir producto: {e}")
            return False