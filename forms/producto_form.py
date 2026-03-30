class ProductoForm:
    def __init__(self, request_form):
        # Captura lo que el usuario escribió en el formulario HTML
        self.nombre = request_form.get('nombre')
        self.precio = request_form.get('precio')
        self.stock = request_form.get('stock')
        self.id_categoria = request_form.get('id_categoria')