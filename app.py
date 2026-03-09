from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import json
import csv

app = Flask(__name__)

# Configuración Base de Datos
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'inventario/data/productos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Postre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

with app.app_context():
    if not os.path.exists('inventario/data'):
        os.makedirs('inventario/data')
    db.create_all()

# --- RUTAS ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def ver_productos():
    lista = Postre.query.all()
    return render_template('productos.html', postres=lista, admin=False)

@app.route('/admin')
def admin_productos():
    lista = Postre.query.all()
    return render_template('productos.html', postres=lista, admin=True)

@app.route('/nuevo_postre', methods=['POST'])
def nuevo_postre():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    stock = int(request.form['stock'])
    precio = float(request.form['precio'])

    # Guardar en SQLite
    nuevo = Postre(nombre=nombre, categoria=categoria, stock=stock, precio=precio)
    db.session.add(nuevo)
    db.session.commit()

    # Guardar en Archivos
    with open('inventario/data/datos.txt', 'a') as f:
        f.write(f"{nombre}, {categoria}, {stock}, {precio}\n")

    with open('inventario/data/datos.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nombre, categoria, stock, precio])

    ruta_json = 'inventario/data/datos.json'
    datos = []
    if os.path.exists(ruta_json):
        with open(ruta_json, 'r') as f:
            try: datos = json.load(f)
            except: datos = []
    datos.append({"nombre": nombre, "categoria": categoria, "stock": stock, "precio": precio})
    with open(ruta_json, 'w') as f: json.dump(datos, f, indent=4)

    return redirect(url_for('admin_productos'))

@app.route('/datos')
def ver_datos():
    productos = Postre.query.all()
    datos_json = []
    if os.path.exists('inventario/data/datos.json'):
        with open('inventario/data/datos.json', 'r') as f:
            try: datos_json = json.load(f)
            except: datos_json = []
    return render_template('datos.html', productos=productos, desde_archivo=datos_json)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    postre = Postre.query.get(id)
    if postre:
        db.session.delete(postre)
        db.session.commit()
    return redirect(url_for('admin_productos'))

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == "__main__":
    app.run(debug=True)