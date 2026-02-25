from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_NAME = 'reposteria.db'

# --- CLASES (POO) ---
class ProductoPostre:
    def __init__(self, id, nombre, categoria, stock, precio):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precio = precio

# --- RUTAS ---

@app.route('/')
def index():
    return render_template('index.html')

# Vista Pública (El docente solo ve esto)
@app.route('/productos')
def ver_productos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()
    conn.close()
    postres = [ProductoPostre(*f) for f in filas]
    return render_template('productos.html', postres=postres, admin=False)

# Vista Privada (Tu ruta secreta para gestionar)
@app.route('/admin')
def admin_productos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()
    conn.close()
    postres = [ProductoPostre(*f) for f in filas]
    return render_template('productos.html', postres=postres, admin=True)

@app.route('/nuevo_postre', methods=['POST'])
def nuevo_postre():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    stock = request.form['stock']
    precio = request.form['precio']
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, categoria, stock, precio) VALUES (?, ?, ?, ?)",
                   (nombre, categoria, stock, precio))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_productos'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin_productos'))

@app.route('/buscar', methods=['POST'])
def buscar():
    consulta = request.form.get('consulta', '')
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%' + consulta + '%',))
    filas = cursor.fetchall()
    conn.close()
    postres = [ProductoPostre(*f) for f in filas]
    return render_template('productos.html', postres=postres, admin=False)

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)