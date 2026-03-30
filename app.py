from flask import Flask, render_template, request, redirect, url_for, send_file
from services.producto_service import ProductoService
from fpdf import FPDF
import os

app = Flask(__name__)

# --- RUTAS PRINCIPALES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

# --- CRUD DE PRODUCTOS ---

@app.route('/productos')
def listar_productos():
    productos = ProductoService.listar_todos()
    # Asegúrate de que el archivo esté en templates/productos/productos.html
    return render_template('productos/productos.html', productos=productos)

@app.route('/productos/crear')
def formulario_crear():
    return render_template('productos/crear_producto.html')

@app.route('/productos/guardar', methods=['POST'])
def guardar_producto():
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']
    
    ProductoService.crear(nombre, precio, stock)
    return redirect(url_for('listar_productos'))

@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    ProductoService.eliminar(id)
    return redirect(url_for('listar_productos'))

# --- SECCIÓN DE FACTURACIÓN (NUEVA) ---

@app.route('/facturas')
def listar_facturas():
    try:
        # Esto usará la nueva función que pusimos en ProductoService
        facturas = ProductoService.listar_facturas()
    except Exception as e:
        print(f"Error al cargar facturas: {e}")
        facturas = []
    # Asegúrate de que el archivo esté en templates/facturas/facturas.html
    return render_template('facturas/facturas.html', facturas=facturas)

# --- GENERACIÓN DE REPORTE PDF ---

@app.route('/reporte_pdf')
def reporte_pdf():
    productos = ProductoService.listar_todos()
    
    pdf = FPDF()
    pdf.add_page()
    
    # Estética del reporte
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "REPORTE DE INVENTARIO - DULCE REPOSTERIA", ln=True, align='C')
    pdf.ln(10)
    
    # Encabezados
    pdf.set_font("Arial", 'B', 12)
    pdf.set_fill_color(255, 182, 193) # Rosado pastel
    pdf.cell(20, 10, "ID", 1, 0, 'C', True)
    pdf.cell(100, 10, "Nombre del Producto", 1, 0, 'C', True)
    pdf.cell(35, 10, "Precio", 1, 0, 'C', True)
    pdf.cell(35, 10, "Stock", 1, 1, 'C', True)
    
    # Datos
    pdf.set_font("Arial", size=12)
    for p in productos:
        pdf.cell(20, 10, str(p['id_producto']), 1)
        pdf.cell(100, 10, p['nombre'], 1)
        pdf.cell(35, 10, f"${p['precio']}", 1)
        pdf.cell(35, 10, str(p['stock']), 1)
        pdf.ln()
    
    nombre_archivo = "reporte_inventario_reposteria.pdf"
    pdf.output(nombre_archivo)
    
    return send_file(nombre_archivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)