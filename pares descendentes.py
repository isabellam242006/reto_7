#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

n= int(input("Ingrese un número natural mayor o igual a dos: "))
while n>=2:
    n -=1
    if n%2!=0:
        continue
    print(n)