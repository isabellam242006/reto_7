
#Imprimir el factorial de un número natural n dado

def calcular_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  
    else:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial

if __name__ == "__main__":
    n = int(input("ingrese un número natural: "))
    factorial=calcular_factorial(n)
print("El factorial de " + str(n) + " es " + str(factorial))

