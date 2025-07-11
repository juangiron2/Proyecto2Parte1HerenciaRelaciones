import uuid
import sys
import os

# Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CRUD.crud_Producto import Listar_productos
from Modelo.Factura import Factura
from CRUD.crud_Cliente import clientes
from CRUD.crud_Producto import productos

facturas = []

def crear_factura():
    cedula_cliente = input("Ingrese la cédula del cliente: ")
    cliente = next((c for c in clientes if c.get_cedula() == cedula_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return

    fecha = input("Ingrese la fecha de la factura (YYYY-MM-DD): ")
    id_factura = str(uuid.uuid4())  # Genera un ID único para la factura

    factura = Factura(cliente, fecha)
    factura.set_id_factura(id_factura)

    while True:
        Listar_productos()
        nombre_producto = input("Ingrese el nombre del producto a agregar (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break

        producto = next((p for p in productos if p.get_nombre() == nombre_producto), None)
        if producto:
            factura.agregar_producto(producto)
        else:
            print("Producto no encontrado.")

    facturas.append(factura)
    cliente.agregar_pedido(factura)
    print(f"Factura creada con éxito. ID de la factura: {id_factura}")

def listar_facturas():
    if not facturas:
        print("No hay facturas registradas.")
    for factura in facturas:
        print(factura)

def actualizar_factura():
    id_factura = input("Ingrese el ID de la factura a actualizar: ")
    factura = next((f for f in facturas if f.get_id_factura() == id_factura), None)
    if not factura:
        print("Factura no encontrada.")
        return

    print("Actualizando factura...")
    nueva_fecha = input("Ingrese la nueva fecha de la factura (YYYY-MM-DD): ")
    factura.set_fecha(nueva_fecha)

    while True:
        print("1. Agregar producto")
        print("2. Terminar actualización")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            Listar_productos()
            nombre_producto = input("Ingrese el nombre del producto a agregar: ")
            producto = next((p for p in productos if p.get_nombre() == nombre_producto), None)
            if producto:
                factura.agregar_producto(producto)
                print(f"Producto {nombre_producto} agregado a la factura.")
            else:
                print("Producto no encontrado.")
        elif opcion == '2':
            break
        else:
            print("Opción no válida.")

    print("Factura actualizada con éxito.")

def eliminar_factura():
    id_factura = input("Ingrese el ID de la factura a eliminar: ")
    for factura in facturas:
        if factura.get_id_factura() == id_factura:
            facturas.remove(factura)
            print(f"Factura con ID {id_factura} eliminada con éxito.")
            return
    print("Factura no encontrada.")
