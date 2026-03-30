from flask import Flask, render_template, redirect, url_for, request, send_file
from services.producto_service import ProductoService
from fpdf import FPDF
import os

app = Flask(__name__)

# RUTA DE INICIO (INDEX)
@app.route('/')
def index():
    return render_template('index.html')

# RUTA PARA VER EL INVENTARIO (Coincide con tu HTML)
@app.route('/productos')
def ver_productos():
    lista = ProductoService.listar_todos()
    return render_template('productos.html', productos=lista)

# RUTA PARA ELIMINAR (Regresa a ver_productos)
@app.route('/eliminar/<int:id>')
def eliminar(id):
    ProductoService.eliminar(id)
    return redirect(url_for('ver_productos'))

# RUTA ACERCA DE (Para que no de error el botón)
@app.route('/acerca')
def acerca():
    return "<h1>Acerca de Nuestra Repostería</h1><p>Sistema de gestión escolar desarrollado para la UEA.</p><a href='/'>Volver al Inicio</a>"

# REPORTE PDF
@app.route('/reporte_pdf')
def reporte_pdf():
    productos = ProductoService.listar_todos()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "Reporte de Inventario - Menú Dulce", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    for p in productos:
        pdf.cell(190, 10, f"ID: {p['id_producto']} | {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}", ln=True)
    
    nombre_archivo = "reporte_reposteria.pdf"
    pdf.output(nombre_archivo)
    return send_file(nombre_archivo, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)