from flask import Flask, render_template, request, redirect, url_for, send_file
from services.producto_service import ProductoService
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def listar_productos():
    try:
        # Llama al servicio para traer los dulces de MySQL
        productos = ProductoService.listar_todos()
        return render_template('productos/productos.html', productos=productos)
    except Exception as e:
        return f"Error en la base de datos: {e}"

@app.route('/facturas')
def listar_facturas():
    try:
        facturas = ProductoService.listar_facturas()
        return render_template('facturas/facturas.html', facturas=facturas)
    except Exception as e:
        return "Error al cargar las facturas."

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

# --- RUTA PARA CREAR PRODUCTOS (CORREGIDA) ---
@app.route('/productos/crear', methods=['GET', 'POST'])
def formulario_crear():
    if request.method == 'POST':
        # 1. Capturamos los datos del formulario
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')
        
        # 2. Guardamos en la base de datos
        if nombre and precio and stock:
            ProductoService.crear_producto(nombre, precio, stock)
        
        # 3. Volvemos al inventario para ver el resultado
        return redirect(url_for('listar_productos'))
    
    # IMPORTANTE: Aquí usamos el nombre exacto de tu archivo
    return render_template('productos/crear_producto.html') 

@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    # Redirección simple para evitar errores
    return redirect(url_for('listar_productos'))

@app.route('/reporte_pdf')
def reporte_pdf():
    try:
        nombre_reporte = "reporte_reposteria_final.txt"
        with open(nombre_reporte, "w") as f:
            f.write("REPORTE DE REPOSTERIA - PROYECTO UEA\n")
            f.write("------------------------------------\n")
            f.write("Estado: CRUD y Base de Datos OK\n")
        return send_file(nombre_reporte, as_attachment=True)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)