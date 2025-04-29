import sys
import os

#Agregar la ruta base del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from CRUD.crud_Cliente import crear_cliente, listar_clientes, actualizar_cliente, eliminar_cliente
from CRUD.crud_Producto import crear_producto, Listar_productos, actualizar_producto, eliminar_producto
from CRUD.crud_Facturas import crear_factura, listar_facturas, actualizar_factura, eliminar_factura

def mostrar_menu():
    print("\n--- Sistema de Facturación ---")
    print("1. Crear Cliente")
    print("2. Listar Clientes")
    print("3. Actualizar Cliente")
    print("4. Eliminar Cliente")
    print("5. Crear Producto")
    print("6. Listar Productos")
    print("7. Actualizar Producto")  
    print("8. Eliminar Producto")
    print("9. Crear Factura")
    print("10. Listar Facturas")
    print("11. Actualizar factura")
    print("12. Eliminar factura")
    print("0. Salir")

def ejecutar_opcion(opcion):

    if opcion == '1':
        crear_cliente()
    elif opcion == '2':
        listar_clientes()
    elif opcion == '3':
        actualizar_cliente()
    elif opcion == '4':
        eliminar_cliente()
    elif opcion == '5':
        crear_producto()
    elif opcion == '6':
        Listar_productos()
    elif opcion == '7':
        actualizar_producto() 
    elif opcion == '8':
        eliminar_producto()
    elif opcion == '9':
        crear_factura()
    elif opcion == '10':
        listar_facturas()
    elif opcion == '11':
        actualizar_factura()
    elif opcion == '12':
        eliminar_factura()
    elif opcion == '0':
        print("Saliendo del sistema...")
    else:
        print("Opción no válida")

def iniciar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_opcion(opcion)
        if opcion == '0':
            break







