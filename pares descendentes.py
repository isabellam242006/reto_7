#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
n = int(input("Ingrese un número natural mayor o igual a dos: "))

if n >= 2:
    while n >= 2:
        if n % 2 == 0:
            print(n)
        n -= 1
else:
    print("El número debe ser mayor o igual a dos.")


    