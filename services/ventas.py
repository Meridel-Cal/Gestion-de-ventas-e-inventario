class Venta:
    def __init__(self):
        """
        Se almacena en una lista porque se necesita tener un registro cronologico y orden de llegadas de 
        las ventas
        """
        self.ventas = []
        
    def registrar_venta(self):
        print("\n[Venta]")
        print("Registrar venta pendiente")
        
    def listar_ventas(self):
        print("\n[Venta]")
        print("Listar ventas pendiente")
        
    def total_vendido(self):
        print("\n[Venta]")
        print("Mostrar total vendido pendiente")
        
    