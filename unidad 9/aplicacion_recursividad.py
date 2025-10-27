

# EJERCICIO: 1 FACTORIAL_RANGO_NUMERO


def factorial(n):
    # Calcula el factorial de un número de forma recursiva.
    # Caso base: el factorial de 0 es 1.
    if n == 0:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# --- Algoritmo principal ---
try:
    numero_limite = int(input("Introduce un numero entero para calcular factoriales: "))
    if numero_limite < 0:
        print("Por favor, introduce un número positivo.")
    else:
        print(f"\nCalculando los factoriales desde 1 hasta {numero_limite}:\n")
        for i in range(1, numero_limite + 1):
            resultado = factorial(i)
            print(f"El factorial de {i} es {resultado}")
except ValueError:
    print("Entrada no valida. Por favor, introduce un numero entero.")


#-----------------------------------------------#-----------------------------------------------------------------------

# EJERCICIO: 2 SUCESION_FIBONACCI

def fibonacci(n):
    # Calcula el valor de la serie de Fibonacci en la posicion n.
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# --- Algoritmo principal ---
try:
    posicion_limite = int(input("Introduce hasta qué posición de la serie de Fibonacci quieres ver: "))
    if posicion_limite < 0:
        print("Por favor, introduce una posición positiva.")
    else:
        print(f"\nLa serie de Fibonacci hasta la posición {posicion_limite} es:")
        for i in range(posicion_limite + 1):
            print(fibonacci(i), end=" ")
        print() # Para un salto de linea al final
except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")


#---------------------------------------------------------------------------------#-----------------------------------



# EJERCICIO: 3 POTENCIA_DE_UN_NUMERO


def potencia(base, exponente):
    # Calcula la potencia de un numero de forma recursiva.
    # Caso base: cualquier numero elevado a 0 es 1.
    if exponente == 0:
        return 1
    # Caso recursivo
    else:
        return base * potencia(base, exponente - 1)

# --- Algoritmo principal ---
try:
    base_num = int(input("Introduce el numero base: "))
    exp_num = int(input("Introduce el exponente: "))
    if exp_num < 0:
        print("Esta función solo admite exponentes positivos.")
    else:
        resultado_potencia = potencia(base_num, exp_num)
        print(f"{base_num} elevado a {exp_num} es igual a {resultado_potencia}")
except ValueError:
    print("Entrada no válida. Por favor, introduce numeros enteros.")



#------------------------------------------------------------------#--------------------------------------------------



# EJERCICIO: 4_CONVERSION_DECIMAL_BINARIO


def decimal_a_binario(n):
    # Convierte un número decimal a su representación binaria como string.
    # Caso base: cuando el cociente es 0, terminamos.
    if n == 0:
        return ""
    # Caso recursivo: se llama con n // 2 y se concatena el resto.
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# --- Algoritmo principal ---
try:
    numero_decimal = int(input("Introduce un numero entero positivo para convertir a binario: "))
    if numero_decimal < 0:
        print("Por favor, introduce un numero positivo.")
    elif numero_decimal == 0:
        print("El binario de 0 es 0.")
    else:
        resultado_binario = decimal_a_binario(numero_decimal)
        print(f"El numero {numero_decimal} en binario es: {resultado_binario}")
except ValueError:
    print("Entrada no valida. Por favor, introduce un número entero.")





 #---------------------------------------------------------------------------#-------------------------------------




 # EJERCICIO: 5 VERIFICADOR_PALINDROMOS


def  es_palindromo(palabra):
    #Verifica si una palabra es un palindromo de forma recursiva.
    # Caso base 1: si la palabra está vacia o tiene 1 letra, es palindromo.
    if len(palabra) <= 1:
        return True
    # Caso base 2: si la primera y ultima letra no coinciden, no es palindromo.
    if palabra[0] != palabra[-1]:
        return False
    # Caso recursivo: llamamos a la funcion con la palabra sin el primer y ultimo caracter.
    return es_palindromo(palabra[1:-1])

# --- Pruebas ---
print(f"¿'neuquen' es palindromo? -> {es_palindromo('neuquen')}")
print(f"¿'reconocer' es palindromo? -> {es_palindromo('reconocer')}")
print(f"¿'python' es palindromo? -> {es_palindromo('python')}")
print(f"¿'a' es palindromo? -> {es_palindromo('a')}")  



#----------------------------------------------------------------------#--------------------------------------------



# EJERCICIO: 6 SUMA_DIGITOS_UN_NUMERO

def suma_digitos(n):
    #Suma los digitos de un numero entero positivo de forma recursiva.
    # Caso base: si n es un numero de un solo digito, lo devuelve.
    if n < 10:
        return n
    # Caso recursivo: suma el ultimo digito con la suma del resto.
    else:
        return (n % 10) + suma_digitos(n // 10)

# --- Pruebas ---
print(f"La suma de los digitos de 1234 es: {suma_digitos(1234)}")
print(f"La suma de los digitos de 9 es: {suma_digitos(9)}")
print(f"La suma de los digitos de 305 es: {suma_digitos(305)}")



#----------------------------------------------------------------------#--------------------------------------------------




# EJERCICIO: 7 PIRAMIDES_BLOQUES


def contar_bloques(n):
    #Calcula el numero total de bloques en una piramide.
    # Caso base: una pirámide con base 1 tiene solo 1 bloque.
    if n == 1:
        return 1
    # Caso recursivo: suma los bloques del nivel actual con los de arriba.
    else:
        return n + contar_bloques(n - 1)

# --- Pruebas ---
print(f"Bloques para una piramide de base 1: {contar_bloques(1)}")
print(f"Bloques para una piramide de base 2: {contar_bloques(2)}")
print(f"Bloques para una piramide de base 4: {contar_bloques(4)}")




#-------------------------------------------------------------#--------------------------------------------------


# EJERCICIO: 8 CONTADOR_DIGITOS

def contar_digito(numero, digito):
    #Cuenta cuántas veces aparece un dígito en un número.
    # Caso base: si el número es 0, ya no hay dígitos que contar.
    if numero == 0:
        return 0

    # Variable para sumar 1 si encontramos el dígito
    contador = 0
    if numero % 10 == digito:
        contador = 1

    # Caso recursivo: sumamos el contador (0 o 1) al resultado
    # de la llamada con el resto del número.
    return contador + contar_digito(numero // 10, digito)

# --- Pruebas ---
print(f"El digito 2 aparece {contar_digito(12233421, 2)} veces en 12233421")
print(f"El digito 5 aparece {contar_digito(5555, 5)} veces en 5555")
print(f"El digito 7 aparece {contar_digito(123456, 7)} veces en 123456")