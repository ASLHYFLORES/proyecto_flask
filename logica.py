import sqlite3

class Producto:
    def __init__(self, id, nombre, categoria, stock, precio):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._stock = stock
        self._precio = precio

    # --- Requisito: Getters (para obtener datos) ---
    @property
    def id(self): return self._id
    @property
    def nombre(self): return self._nombre
    @property
    def categoria(self): return self._categoria
    @property
    def stock(self): return self._stock
    @property
    def precio(self): return self._precio

    # --- Requisito: Setters (para actualizar datos) ---
    @stock.setter
    def stock(self, nuevo_valor): self._stock = nuevo_valor
    @precio.setter
    def precio(self, nuevo_valor): self._precio = nuevo_valor

class Inventario:
    def __init__(self):
        self.db_name = 'reposteria.db'
        self.productos_dict = {} # REQUISITO: Uso de Diccionario

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def cargar_desde_db(self):
        """Carga datos de SQLite al Diccionario del programa"""
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()
        # Llenamos el diccionario usando el ID como llave
        self.productos_dict = {f[0]: Producto(*f) for f in filas}
        conn.close()
        return self.productos_dict.values()

    def añadir(self, nombre, categoria, stock, precio):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, categoria, stock, precio) VALUES (?,?,?,?)",
                       (nombre, categoria, stock, precio))
        conn.commit()
        conn.close()

    def eliminar(self, id_p):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_p,))
        conn.commit()
        conn.close()

    def buscar(self, nombre_buscado):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre_buscado + '%',))
        filas = cursor.fetchall()
        conn.close()
        return [Producto(*f) for f in filas]