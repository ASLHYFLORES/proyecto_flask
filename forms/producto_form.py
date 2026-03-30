class ProductoForm:
    def __init__(self, request_form):
        # Capturamos los datos que vienen del formulario HTML
        self.nombre = request_form.get('nombre')
        self.precio = request_form.get('precio')
        self.stock = request_form.get('stock')
        self.id_categoria = request_form.get('id_categoria')

    def es_valido(self):
        # Una validación básica: que el nombre y el precio no estén vacíos
        if not self.nombre or not self.precio:
            return False
        return True