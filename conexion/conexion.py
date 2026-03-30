import sys
import os

# Esto busca el archivo conexion.py que tienes afuera
ruta_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_padre not in sys.path:
    sys.path.insert(0, ruta_padre)

try:
    from conexion import obtener_conexion
except ImportError:
    # Si falla, intentamos importarlo directamente
    import conexion
    obtener_conexion = conexion.obtener_conexion

class ProductoService:
    @staticmethod
    def listar_todos():
        conn = obtener_conexion()
        if conn is None:
            return []
        try:
            # dictionary=True arregla el error de "tuple object"
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en listar_todos: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def listar_facturas():
        conn = obtener_conexion()
        if conn is None:
            return []
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT f.id_factura, c.nombre AS cliente, p.nombre AS producto, 
                       f.cantidad, f.total, f.fecha 
                FROM facturas f
                JOIN clientes c ON f.id_cliente = c.id_cliente
                JOIN productos p ON f.id_producto = p.id_producto
                ORDER BY f.fecha DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en listar_facturas: {e}")
            return []
        finally:
            conn.close()