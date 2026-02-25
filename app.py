from flask import Flask, render_template, request, redirect, url_for
from logica import Inventario

app = Flask(__name__)
gestion = Inventario()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def ver_productos():
    lista = gestion.cargar_desde_db()
    return render_template('productos.html', postres=lista, admin=False)

@app.route('/admin')
def admin_productos():
    lista = gestion.cargar_desde_db()
    return render_template('productos.html', postres=lista, admin=True)

@app.route('/nuevo_postre', methods=['POST'])
def nuevo_postre():
    gestion.añadir(request.form['nombre'], request.form['categoria'], 
                   request.form['stock'], request.form['precio'])
    return redirect(url_for('admin_productos'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    gestion.eliminar(id)
    return redirect(url_for('admin_productos'))

@app.route('/buscar', methods=['POST'])
def buscar():
    query = request.form.get('consulta', '')
    lista = gestion.buscar(query)
    return render_template('productos.html', postres=lista, admin=False)

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

if __name__ == '__main__':
    app.run(debug=True)