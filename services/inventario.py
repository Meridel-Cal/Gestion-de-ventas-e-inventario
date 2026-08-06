class Inventario:
    def __init__(self):
        """
        Inventario en estructura de lista, orden e insercion
        """
        self.productos = []
        
    def registrar_producto(self):
        """
        Registra un producto en el inventario.
        """
        print("\n[Inventario]")
        print("Registrar producto pendiente")
        
    def listar_productos(self):
        print("\n[Inventario]")
        print("Listar productos pendiente")
        
    def buscar_producto(self):
        print("\n[Inventario]")
        print("Buscar producto pendiente")
        
    def eliminar_producto(self):
        print("\n[Inventario]")
        print("Eliminar producto pendiente")
        
    def mostrar_cantidad_productos(self):
        """
        Este metodo se puede implementar si queremos saber cuantos productos hay en el inventario, pero no es necesario ya que podemos usar len() para obtener la cantidad de productos en la lista.
        """
        print("Mostrar cantidad de productos pendiente")