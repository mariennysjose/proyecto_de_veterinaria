"""
Dr. Gregory Cat (Diagnostico Veterinario)
Para el hospital Universitario Princeton-Plainsboro de Nueva Jersey.
Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden
atender 15 mascotas), para esto hay que considerar los siguientes datos y
encasillarlos en ciertos diagnósticos para poder derivarlos adecuadamente:
● Edad (Validar entre 1 y 20 años)
● Tipo: (Validar “gato”, “perro”, “hámster”)
● Peso: (Más de 0 kg)
● Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
● Vacuna antirrábica (validar “si”, ”no”)
Tema A
1. Cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10
años, que se presentaron por problemas digestivos o parásitos.
2. El tipo de mascota más ingresada con problemas digestivos.
3. Edad y tipo de la mascota más vieja sin vacuna antirrábica.
4. Porcentaje de mascotas vacunadas y no vacunadas.
5. Promedio de edad de los perros.

"""
#variables
otra_mascota = 0
contador_vacu_antirrabica=0
edad_mascota_mas_vieja=0
contador_vacunado=0
contador_no_vacunado=0
contador_perro=0
suma_edades_perro = 0


#iniciacion del programa

while otra_mascota <= 15:
    otra_mascota += 1
    
    nombre = input("Ingrese nombre: ")

    while True:
        edad = int(input("Ingrese edad de la mascota (Validar entre 1 y 20 años): "))
        if 1 <= edad and edad <= 20:
            break
    while True:
        tipo = input("(Validar “gato”, “perro”, “hámster”): ")
        if tipo == "gato" or tipo == "perro" or tipo == "hamster":
            break
        else:
            print("eleccion invalida")

    while True:
        peso = int(input("Más de 0 kg: "))
        if peso > 0:
            break

    while True:
        diasnostico = input("Validar “problemas digestivos”, “parásitos”, “infección”: ")
        if diasnostico == "problemas digestivos" or diasnostico == "parasitos" or diasnostico == "infeccion":
            break

    while True:
        vacuna = input("Vacuna antirrábica (validar “si”, ”no”: )")
        if vacuna == "si" or vacuna == "no":
            break

#Cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10 años, que se presentaron por problemas digestivos o parásitos.

    if vacuna == "si" and 5 <= edad <=10 and diasnostico == "problemas digestivos" or diasnostico== "parasitos":
        contador_vacu_antirrabica += 1   

#El tipo de mascota más ingresada con problemas digestivos.

    if tipo == "gato" or tipo == "perro" or tipo== "hamster" and diasnostico == "problemas digestivos":
            tipo_mas_ingresada = tipo
     
#Edad y tipo de la mascota más vieja sin vacuna antirrábica.
    
    if edad > edad_mascota_mas_vieja and tipo == "gato" or tipo == "hamster" or tipo =="perro" and vacuna == "no":
        edad_mascota_mas_vieja = edad
        tipo_mascota_mas_vieja = tipo

#Porcentaje de mascotas vacunadas y no vacunadas

    if vacuna == "si":
        contador_vacunado += 1
    else:
        contador_no_vacunado +=1

    # Calculamos el total de mascotas

    total_mascotas = contador_vacunado + contador_no_vacunado
    
    # Calculamos los porcentajes

    if total_mascotas > 0:
        porcentaje_vacunados = (contador_vacunado / total_mascotas) * 100
        porcentaje_no_vacunados = (contador_no_vacunado / total_mascotas) * 100


#Promedio de edad de los perros
if tipo == "perro":
    contador_perro += 1
    suma_edades_perro += edad

if contador_perro > 0:
     promedio_edad_perros = suma_edades_perro / contador_perro


#resultados

print("Cantidad de mascotas con vacuna antirrábica, cuya edad está entre los 5 y 10 años, que se presentaron por problemas digestivos o parásitos.")
print(contador_vacu_antirrabica)
print("El tipo de mascota más ingresada con problemas digestivos")
print(tipo_mas_ingresada)
print("Edad y tipo de la mascota más vieja sin vacuna antirrábica.")
print(edad_mascota_mas_vieja)
print(tipo_mascota_mas_vieja)
print("Porcentaje de mascotas vacunadas y no vacunadas")
print("Vacunadas")
print(porcentaje_vacunados)
print("No Vacunadas")
print(porcentaje_no_vacunados)
print("Promedio de edad de los perros")
print(promedio_edad_perros)




























