@staticmethod
    def listar_facturas():
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                # Esta consulta une las 3 tablas para mostrar nombres en lugar de IDs
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
                # Retorna todos los registros encontrados
                return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar facturas: {e}")
            return []
        finally:
            # Muy importante cerrar la conexión para evitar errores de MySQL
            conexion.close()