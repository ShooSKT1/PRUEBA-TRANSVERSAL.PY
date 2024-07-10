import random
import csv




    
# Lista de nombres de los empleados
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para generar sueldos aleatorios
def generar_sueldos(num_empleados, sueldo_min=300000, sueldo_max=2500000):
    sueldos = []
    for _ in range(num_empleados):
        sueldo = random.randint(sueldo_min, sueldo_max)
        sueldos.append(sueldo)
    return sueldos

# Generar los sueldos para los 10 empleados
sueldos_generados = generar_sueldos(len(trabajadores))

# Mostrar los nombres de los empleados con sus sueldos generados
print("Análisis de sueldos de empleados:")
for i in range(len(trabajadores)):
    print(f"{trabajadores[i]}: ${sueldos_generados[i]:,.2f}")
    
    def clasificar_sueldos(lista_empleados):
    # Inicialización de contadores y listas para cada categoría
    sueldos_bajos = []
    sueldos_medios = []
    sueldos_altos = []
    
    total_sueldos = 0
    
    # Clasificación de los empleados según su sueldo
    for empleado, sueldo in lista_empleados:
        total_sueldos += sueldo
        if sueldo < 800000:
            sueldos_bajos.append((empleado, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            sueldos_medios.append((empleado, sueldo))
        else:
            sueldos_altos.append((empleado, sueldo))
    
    # Mostrar resultados
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(sueldos_bajos)}")
    print("Nombre empleado Sueldo")
    for empleado, sueldo in sueldos_bajos:
        print(f"{empleado} ${sueldo}")
    print()
    
    print("Sueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(sueldos_medios)}")
    print("Nombre empleado Sueldo")
    for empleado, sueldo in sueldos_medios:
        print(f"{empleado} ${sueldo}")
    print()
    
    print("Sueldos superiores a $2.000.000")
    print(f"TOTAL: {len(sueldos_altos)}")
    print("Nombre empleado Sueldo")
    for empleado, sueldo in sueldos_altos:
        print(f"{empleado} ${sueldo}")
    print()
    
    print(f"TOTAL SUELDOS: ${total_sueldos}")

# Ejemplo de uso
empleados = [
    ("Juan Pérez", 500000),
    ("María García", 700000),
    ("Pedro Soto", 1100000),
    ("Isabel Gómez", 800000),
    ("Miguel Sánchez", 2100000)
]

clasificar_sueldos(empleados)




