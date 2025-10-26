
# JERCICIO 1: PRECIOS_FRUTAS


precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)
# Salida: {'Banana': 1200, 'Anana': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}


#-----------------------------------------------------------#----------------------------------------------------------------------


#EJERCICIO: 2 ACTUALIZAR_PRECIOS

# Usamos el diccionario del punto anterior
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)
# Salida: {'Banana': 1330, 'Anana': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}


#-----------------------------------------------------------#-----------------------------------------------------------------------


#EJERCICO: 3 LISTA_DE_FRUTAS 

# Usamos el diccionario del punto anterior
lista_de_frutas = list(precios_frutas.keys())

print(lista_de_frutas)
# Salida: ['Banana', 'Anana', 'Melon', 'Uva', 'Naranja', 'Manzana', 'Pera']

#EJERCICIO:4 AGENDA_NUMEROS_TEL

contactos = {}

# Cargar 5 contactos
print("--- Cargar Contactos ---")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

print("\n--- Consultar Contacto ---")
nombre_consulta = input("Ingrese el nombre del contacto que desea buscar: ")

# Mostrar el número usando .get() que devuelve None si no encuentra la clave
numero_encontrado = contactos.get(nombre_consulta)

if numero_encontrado:
    print(f"El numero de {nombre_consulta} es: {numero_encontrado}")
else:
    print(f"El contacto {nombre_consulta} no se encuentra en la agenda.")




#------------------------------------------------------#--------------------------------------------------------



#EJERCICIO: 6 PROMEDIO_NOTAS


alumnos_notas = {}

for _ in range(3):
    nombre = input(f"\nIngrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)
    # Guardamos las notas como una tupla
    alumnos_notas[nombre] = tuple(notas)

print("\n--- Promedios de los Alumnos ---")
for nombre, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: tiene un promedio de {promedio:.2f}") # .2f formatea a 2 decimales



#--------------------------------------------------------------------#-------------------------------------------------------------


#EJERCICIO: 7 PARCIALES_DE_ESTUDUANTES

parcial1 = {'Ana', 'Marcos', 'Pedro', 'Sofia', 'Luis'}
parcial2 = {'Marcos', 'Carla', 'Pedro', 'Juan', 'Ana'}

# 1. Aprobaron ambos (Intersección)
ambos_parciales = parcial1.intersection(parcial2) # Tambien se puede usar: parcial1 & parcial2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

# 2. Aprobaron solo uno de los dos (Diferencia simetrica)
solo_un_parcial = parcial1.symmetric_difference(parcial2) # Tambien se puede usar: parcial1 ^ parcial2
print(f"Estudiantes que aprobaron solo un parcial: {solo_un_parcial}")

# 3. Lista total de aprobados (Unión)
todos_aprobados = parcial1.union(parcial2) # Tambien se puede usar: parcial1 | parcial2
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {todos_aprobados}")



#--------------------------------------------------------------------------------#---------------------------------------------------------------


#EJERCICIO: 8 STOCK

stock = {'tornillos': 100, 'tuercas': 150, 'clavos': 80}

while True:
    print("\n--- Gestion de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar producto/stock")
    print("3. Salir")
    opcion = input("Elija una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ")
        # Usamos .get() para evitar errores si el producto no existe
        cantidad = stock.get(producto, "Producto no encontrado")
        print(f"Stock de {producto}: {cantidad}")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input(f"Ingrese la cantidad a agregar: "))
        
        if producto in stock:
            # Si ya existe, suma al stock actual
            stock[producto] += cantidad
            print(f"Stock de {producto} actualizado a {stock[producto]}.")
        else:
            # Si no existe, lo crea
            stock[producto] = cantidad
            print(f"Producto {producto} agregado con un stock de {cantidad}.")
            
    elif opcion == '3':
        print("Saliendo del programa.")
        break
        
    else:
        print("Opcion no valida. Intente de nuevo.")





#----------------------------------------------------------------------------#-----------------------------------------------------------------------



#EJERCICIO: 9 AGENDA_EVENTOS

agenda = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Miércoles', '15:30'): 'Cita con el dentista',
    ('Viernes', '21:00'): 'Cena con amigos'
}

# Consultar una actividad
dia_consulta = input("Ingrese el día (ej: Lunes): ").capitalize()
hora_consulta = input("Ingrese la hora (ej: 10:00): ")

# Creamos la tupla para buscar en el diccionario
clave_consulta = (dia_consulta, hora_consulta)

evento = agenda.get(clave_consulta, "No hay ninguna actividad programada.")
print(f"Actividad para el {dia_consulta} a las {hora_consulta}: {evento}")



#-----------------------------------------------------------------------------#--------------------------------------------------------------------


#EJERCICIO: 10 INVERTIR_DICC. (PAISES CAPITALES)

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma'
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario original:")
print(paises_capitales)
print("\nDiccionario invertido:")
print(capitales_paises)
# Salida del invertido: {'Buenos Aires': 'Argentina', 'Madrid': 'España', 'París': 'Francia', 'Roma': 'Italia'}

