import sqlite3

def crear_tablas():
    conn = sqlite3.connect('reposteria.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            stock INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Base de Datos lista para la Repostería.")

if __name__ == "__main__":
    crear_tablas()