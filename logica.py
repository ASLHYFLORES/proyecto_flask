import sqlite3

class Producto:
    def __init__(self, id, nombre, categoria, stock, precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precio = precio

class Inventario:
    def __init__(self):
        self.db_name = 'reposteria.db'
        # Usamos un DICCIONARIO para cumplir con el requisito
        self.productos_dict = {}

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def cargar_desde_db(self):
        """Carga los datos de SQLite al Diccionario de la clase"""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()
        # Llenamos el diccionario: { id: Objeto_Producto }
        self.productos_dict = {f[0]: Producto(*f) for f in filas}
        conn.close()

    def añadir(self, nombre, categoria, stock, precio):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, categoria, stock, precio) VALUES (?,?,?,?)",
                       (nombre, categoria, stock, precio))
        conn.commit()
        conn.close()
        self.cargar_desde_db()

    def eliminar(self, id_producto):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        conn.close()
        if id_producto in self.productos_dict:
            del self.productos_dict[id_producto]

    def actualizar(self, id_producto, nuevo_stock, nuevo_precio):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET stock = ?, precio = ? WHERE id = ?", 
                       (nuevo_stock, nuevo_precio, id_producto))
        conn.commit()
        conn.close()
        self.cargar_desde_db()