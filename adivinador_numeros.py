import random

print("Piense en un número de 1 a 100")
numero_minimo = 1
numero_maximo = 100
num_random = random.randrange(numero_minimo, numero_maximo)
bandera = True

while bandera or respuesta != "igual":
    bandera = False
    respuesta = input("El número " + str(num_random) + " es igual, mayor o menor que el número en el que pensó. Ponga solo la palabra, todo en minúsculas: ")
    if respuesta == "mayor":
        numero_maximo = num_random 
        num_random = random.randrange(numero_minimo, numero_maximo)
    elif respuesta == "menor":
        numero_minimo = num_random 
        num_random = random.randrange(numero_minimo, numero_maximo)
    elif respuesta =="igual":
      print("El número que has pensado es " + str(num_random))
    else:
      print("Recuerda escribir todo en minúsculas, revisa que hayas escrito correctamente la palabra")