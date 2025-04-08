from modelo.Factura import Factura
from modelo.Cliente import Cliente
from modelo.Control_plagas import ControlPlagas
from modelo.Control_fertilizante import ControlFertilizantes
from modelo.Antibiotico import Antibiotico

def main():
    # Crear un cliente
    cliente = Cliente("Juan Pérez", "123456789")
    
    # Crear una factura para el cliente
    factura = Factura(cliente, "2024-10-18")
    
    # Crear diferentes tipos de productos
    plaga = ControlPlagas("Fungicida", 10000, "ICA123", 15, 7)
    fertilizante = ControlFertilizantes("SuperGrow", 15000, "ICA456", 30, "2024-09-01")
    antibiotico = Antibiotico("AntiPig", 20000, 500, "Porcino")
    
    # Agregar productos a la factura
    factura.agregar_producto(plaga)
    factura.agregar_producto(fertilizante)
    factura.agregar_producto(antibiotico)
    
    # Agregar la factura al cliente
    cliente.agregar_pedido(factura)
    
    # Imprimir la factura
    print(factura)
    
    # Crear otra factura para el mismo cliente
    factura2 = Factura(cliente, "2024-10-20")
    factura2.agregar_producto(plaga)
    cliente.agregar_pedido(factura2)
    
    # Imprimir todas las facturas del cliente
    print("\nFacturas del cliente:")
    for factura in cliente.pedidos:
        print(factura)
    
    # Imprimir información del cliente
    print("\nInformación del cliente:")
    print(cliente)
    print(f"Total de compras: ${cliente.obtener_total_compras():.2f}")

if __name__ == "__main__":
    main()
