import time
import random

#Funcion de ordenamiento tipo bubble sort
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


#Funcion de ordenamiento tipo insertion sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave

#Funcion de ordenamiento tipo selection sort
def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

#Funcion de busqueda tipo lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

#Funcion de busqueda tipo binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


#Funcion encargada de procesar los datos
def procesar_datos(numAProcesar):
    print("______________________________________________")
    #Imprime la cantidad de elementos que se van a procesar
    print(f"Pruebas realizadas con {numAProcesar} elementos")

    #Genera una lista de numeros aleatorios entre 1 y 10000 del tamaño indicado
    datos_original = [random.randint(1, 10000) for _ in range(numAProcesar)]

    #Objetivo a buscar
    objetivo = datos_original[numAProcesar // 2]
    
    #Itera sobre una lista que contiene todos los algoritmos de ordenamientos y su funcion
    for algoritmo in [("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort), ("Selection Sort", selection_sort)]:
        #Creamos una copia de los datos originales para no modificar la lista base
        datos = datos_original.copy()

        #Tomamos el tiempo de inicio antes de ejecutar el algoritmo
        inicio = time.time()
        
        #Ejecutamos el algoritmo de ordenamiento sobre la copia
        algoritmo[1](datos)

        #Calcula el tiempo que tardo en ejecutarse el algoritmo y luego lo imprimimos en pantalla
        duracion = time.time() - inicio
        print(f"{algoritmo[0]}: {duracion:.6f} segundos")

    #Ordenamos la lista original
    datos_ordenados = sorted(datos_original)

    #Medimos el tiempo que tarda en hacer la busqueda binaria
    inicio = time.time()
    busqueda_binaria(datos_ordenados, objetivo)
    print(f"Búsqueda Binaria: {(time.time() - inicio):.6f} segundos")

    #Medimos el tiempo que tarda en hacer la busqueda lineal
    inicio = time.time()
    busqueda_lineal(datos_original, objetivo)
    print(f"Búsqueda Lineal: {(time.time() - inicio):.6f} segundos")

#Funcion principal, encargada de mostrar el menu 
def menu_interactivo():
    print(" _____________________________________________________________________________________")
    print("|                                                                                     |")
    print("|Bienvenido! Analizaremos los tiempos de procesamiento de distintas tipos de busquedas|")
    print("|_____________________________________________________________________________________|")
    
    #Loop solicitando el ingreso de la cantidad de numeros a procesar.
    while True:
        #Imprimimos la pregunta en pantalla, debe ser mayor a 0
        try:
            numAProcesar = int(input("Cuántos números querés procesar? "))
            if numAProcesar <= 0:
                raise ValueError("Debe ser un número entero positivo.")
        
        #Captura de errores
        except ValueError as e:
            print(f"Entrada no válida: Debe ser un número entero positivo.")
            continue
        
        #Llamamos la funcion encargada de procesar los datos
        procesar_datos(numAProcesar)

        #Consultamos al usuario si desea procesar otra lista
        respuesta = input("Querés procesar otra lista? (s/n): ").strip().lower()
        if respuesta != 's':
            print("Programa finalizado.")
            break

#Ejecucion
menu_interactivo()
