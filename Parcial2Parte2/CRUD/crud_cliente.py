import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.Cliente import Cliente

clientes = []

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    print(f"Cliente {nombre} creado con éxito.")

def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
    for cliente in clientes:
        print(cliente)

def actualizar_cliente():
    cedula = input("Ingrese la cédula del cliente a actualizar: ")
    for cliente in clientes:
        if cliente.cedula == cedula:
            nuevo_nombre = input(f"Nuevo nombre para el cliente (anterior: {cliente.nombre}): ")
            cliente.nombre = nuevo_nombre
            print("Cliente actualizado con éxito.")
            return
    print("Cliente no encontrado.")

def eliminar_cliente():
    cedula = input("Ingrese la cédula del cliente a eliminar: ")
    for cliente in clientes:
        if cliente.cedula == cedula:
            clientes.remove(cliente)
            print(f"Cliente con cédula {cedula} eliminado.")
            return
    print("Cliente no encontrado.")

