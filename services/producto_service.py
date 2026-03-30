from conexion.conexion import obtener_conexion

class ProductoService:
    @staticmethod
    def listar_todos():
        db = obtener_conexion()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos")
            datos = cursor.fetchall()
            db.close()
            return datos
        return []

    @staticmethod
    def insertar(nombre, precio, stock, id_cat):
        db = obtener_conexion()
        if db:
            cursor = db.cursor()
            sql = "INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, precio, stock, id_cat))
            db.commit()
            db.close()

    @staticmethod
    def eliminar(id_p):
        db = obtener_conexion()
        if db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_p,))
            db.commit()
            db.close()