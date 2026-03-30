from conexion.conexion import obtener_conexion

class ProductoService:
    @staticmethod
    def listar_todos():
        db = obtener_conexion()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        db.close()
        return datos

    @staticmethod
    def eliminar(id_p):
        db = obtener_conexion()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_p,))
        db.commit()
        db.close()