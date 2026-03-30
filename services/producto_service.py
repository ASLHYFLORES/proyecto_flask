from conexion import obtener_conexion

class ProductoService:
    @staticmethod
    def listar_facturas():
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                query = """
                    SELECT 
                        f.id_factura, 
                        c.nombre AS cliente, 
                        p.nombre AS producto, 
                        f.cantidad, 
                        f.total, 
                        f.fecha 
                    FROM facturas f
                    JOIN clientes c ON f.id_cliente = c.id_cliente
                    JOIN productos p ON f.id_producto = p.id_producto
                    ORDER BY f.fecha DESC
                """
                cursor.execute(query)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error al cargar facturas: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def listar_todos():
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM productos")
                return cursor.fetchall()
        finally:
            conexion.close()