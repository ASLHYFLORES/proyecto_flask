from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/productos')
def productos():
    items = ['Producto 1', 'Producto 2', 'Producto 3']
    return render_template('productos.html', lista=items) # Revisa que 'lista' coincida con tu HTML

if __name__ == '__main__':
    app.run(debug=True)