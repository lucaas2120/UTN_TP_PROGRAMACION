# Lista precargada de estudiantes
estudiantes = [
    {"nombre": "Juan Pérez", "legajo": 1001},
    {"nombre": "María Gómez", "legajo": 1002},
    {"nombre": "Carlos Díaz", "legajo": 1003},
    {"nombre": "Ana Torres", "legajo": 1004},
    {"nombre": "Lucía Ramírez", "legajo": 1005},
    {"nombre": "Juan Carlos", "legajo": 1006},
    {"nombre": "Ana María", "legajo": 1007},
    {"nombre": "Jorge Atencio", "legajo": 1501},
    {"nombre": "Lucas Alvarez", "legajo": 1830},
]

# Función de búsqueda lineal por nombre (parcial o completo)
def buscar_por_nombre(nombre_buscado):
    resultados = []
    for estudiante in estudiantes:
        if nombre_buscado.lower() in estudiante["nombre"].lower():
            resultados.append(estudiante)
    return resultados

# Función de búsqueda lineal por legajo
def buscar_por_legajo(legajo_buscado):
    for estudiante in estudiantes:
        if estudiante["legajo"] == legajo_buscado:
            return estudiante
    return None

# Menú principal
def main():
    while True:
        print("\n--- Menú de Búsqueda de Estudiantes ---")
        print("1. Buscar por nombre (parcial o completo)")
        print("2. Buscar por legajo")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre o parte del nombre: ")
            resultados = buscar_por_nombre(nombre)
            if resultados:
                print("\nEstudiantes encontrados:")
                for est in resultados:
                    print(f"- {est['nombre']} (Legajo: {est['legajo']})")
            else:
                print("No se encontraron coincidencias.")
        elif opcion == "2":
            try:
                legajo = int(input("Ingrese el número de legajo: "))
                resultado = buscar_por_legajo(legajo)
                if resultado:
                    print(f"\nEstudiante encontrado: {resultado['nombre']} (Legajo: {resultado['legajo']})")
                else:
                    print("Estudiante no encontrado.")
            except ValueError:
                print("Por favor, ingrese un número de legajo válido.")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()