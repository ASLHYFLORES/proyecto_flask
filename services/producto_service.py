from conexion.conexion import obtener_conexion

class ProductoService:
    
    @staticmethod
    def listar_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos

    @staticmethod
    def crear(nombre, precio, stock):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        # id_categoria se enviará como NULL por defecto o puedes quemar un ID (ej. 1)
        sql = "INSERT INTO productos (nombre, precio, stock, id_categoria) VALUES (%s, %s, %s, 1)"
        valores = (nombre, precio, stock)
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM productos WHERE id_producto = %s"
        cursor.execute(sql, (id_producto,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def listar_facturas():
        """Obtiene la unión de Clientes, Productos y Facturas"""
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        sql = """
            SELECT f.id_factura, c.nombre_completo AS cliente, 
                   p.nombre AS producto, f.cantidad, f.total, f.fecha_emision
            FROM facturas f
            JOIN clientes c ON f.id_cliente = c.id_cliente
            JOIN productos p ON f.id_producto = p.id_producto
        """
        cursor.execute(sql)
        facturas = cursor.fetchall()
        conexion.close()
        return facturas