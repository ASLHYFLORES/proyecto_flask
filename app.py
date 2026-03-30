from flask import Flask, render_template, request, redirect, url_for, send_file
from services.producto_service import ProductoService
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def listar_productos():
    lista = ProductoService.listar_todos()
    return render_template('productos.html', productos=lista)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    ProductoService.eliminar(id)
    return redirect(url_for('listar_productos'))

@app.route('/reporte_pdf')
def reporte_pdf():
    productos = ProductoService.listar_todos()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(190, 10, "Menú Dulce - Reporte de Inventario", ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    for p in productos:
        pdf.cell(190, 10, f"ID: {p['id_producto']} | {p['nombre']} | Stock: {p['stock']} | ${p['precio']}", ln=True)
    
    pdf.output("reporte.pdf")
    return send_file("reporte.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)