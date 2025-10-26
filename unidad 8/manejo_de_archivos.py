#EJERCICIO: 1 ARCHIVO_INICIAL_PRODUCTOS


def crear_archivo_inicial():
    """Crea el archivo productos.txt si no existe y escribe tres productos iniciales."""
    try:
        # Se abre en modo 'x' para crear el archivo solo si no existe
        # y evitar sobrescribir datos accidentalmente.
        with open("productos.txt", "x") as archivo:
            archivo.write("Lapicera,120.50,30\n")
            archivo.write("Cuaderno,250.00,15\n")
            archivo.write("Goma,80.75,50\n")
        print("Archivo 'productos.txt' creado con éxito.")
    except FileExistsError:
        # Si el archivo ya existe, no hacemos nada.
        print("El archivo 'productos.txt' ya existe. No se ha modificado.")




#EJERCICIO: 2,4 y 5 (leer cargar y buscar productos)


def cargar_productos():
    """Lee el archivo y carga los productos en una lista de diccionarios."""
    productos = []
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                # Limpiamos la línea y la separamos por la coma
                nombre, precio, cantidad = linea.strip().split(",")
                producto = {
                    "nombre": nombre,
                    "precio": float(precio), # Convertimos a numero flotante
                    "cantidad": int(cantidad)  # Convertimos a numero entero
                }
                productos.append(producto)
    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró.")
    return productos

def mostrar_productos(productos):
    """Muestra la lista de productos con un formato específico."""
    print("\n--- Listado de Productos ---")
    if not productos:
        print("No hay productos para mostrar.")
        return
    for prod in productos:
        print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Cantidad: {prod['cantidad']}")
    print("--------------------------\n")

def buscar_producto(productos):
    """Pide un nombre de producto y muestra sus datos si lo encuentra."""
    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
    encontrado = False
    for prod in productos:
        if prod['nombre'].lower() == nombre_buscado:
            print("\n--- Producto Encontrado ---")
            print(f"Nombre: {prod['nombre']}")
            print(f"Precio: ${prod['precio']:.2f}")
            print(f"Cantidad: {prod['cantidad']}")
            print("-------------------------\n")
            encontrado = True
            break # Terminamos el bucle porque ya lo encontramos
    
    if not encontrado:
        print(f"\nError: El producto '{nombre_buscado}' no se encuentra en la lista.\n")



#EJERCICIO: 3 y 6 (agregar y guardar productos)



def agregar_producto_interactivo():
    """Pide datos al usuario y los agrega al final del archivo."""
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    
    # Abrimos en modo 'a' (append) para agregar al final sin borrar.
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    print(f"¡Producto '{nombre}' agregado con éxito!\n")

def guardar_productos_actualizados(productos):
    """Sobrescribe el archivo con la lista de productos actualizada."""
    # Abrimos en modo 'w' (write) para borrar el contenido y escribir de nuevo.
    with open("productos.txt", "w") as archivo:
        for prod in productos:
            archivo.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")
    print("Todos los productos han sido guardados en 'productos.txt'.")



#programa principal


def main():
    """Función principal que ejecuta el menú interactivo."""
    crear_archivo_inicial() # Preparamos el archivo si es la primera vez
    
    while True:
        print("\n===== GESTIÓN DE PRODUCTOS =====")
        print("1. Mostrar todos los productos")
        print("2. Agregar un nuevo producto")
        print("3. Buscar un producto por nombre")
        print("4. Guardar y Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            lista_prods = cargar_productos()
            mostrar_productos(lista_prods)
        
        elif opcion == '2':
            agregar_producto_interactivo()

        elif opcion == '3':
            lista_prods = cargar_productos() # Cargamos la lista actualizada
            buscar_producto(lista_prods)
        
        elif opcion == '4':
            lista_prods = cargar_productos() # Cargamos la lista actualizada antes de salir
            guardar_productos_actualizados(lista_prods)
            print("Programa finalizado.")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

