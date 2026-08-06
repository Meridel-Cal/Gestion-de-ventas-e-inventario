from utils.menu import mostrar_menu
from services.inventario import Inventario
from services.ventas import Venta

def main():
    #Dependencias de la clase main
    inventario = Inventario() #Instanciar la clase inventario
    ventas = Venta() #Instanciar la clase venta
    
    while True:
        opcion = mostrar_menu()
        
        match opcion:
            case "1":
                inventario.registrar_producto()
            case "2":
                inventario.listar_productos()
            case "3":
                inventario.buscar_producto()
            case "4":
                inventario.eliminar_producto()
            case "5":
                ventas.registrar_venta()
            case "6":
                ventas.listar_ventas()
            case "7":
                ventas.total_vendido()
            case "8":
                print("\nSaliendo del sistema...")
                break
            case _:
                print("\nOpción inválida. Por favor, seleccione una opción válida.")
                
                
main()