import sys
import os

# Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modelo.Producto import Productos

productos = []

def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    producto = Productos(nombre, precio)
    productos.append(producto)
    print(f"Producto '{producto.get_nombre()}' creado con éxito.")

def Listar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            print(producto)

def actualizar_producto():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto.get_nombre() == nombre:
            nuevo_nombre = input(f"Nuevo nombre para el producto (anterior: {producto.get_nombre()}): ")
            nuevo_precio = float(input(f"Nuevo precio para el producto (anterior: {producto.get_precio()}): "))
            producto.set_nombre(nuevo_nombre)
            producto.set_precio(nuevo_precio)
            print("Producto actualizado con éxito.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto.get_nombre() == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print("Producto no encontrado.")
