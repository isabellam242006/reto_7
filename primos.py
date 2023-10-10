def calcular_numeros_primos(n):  #Definimos función
    while n <= 100:              #Hasta que n sea menor o igual que 100
        i = 2                    #Definimos i desde 2, ya que si lo definimos desde 1 sabemos que no podremos saber si n es un número es primo
        es_primo = True          #Definimos la función como verdadera
        while i < n:             #Desde que n sea mayor que i:
            if n % i == 0:       #Si el cociente entre n e i es cero
                es_primo = False #Entonces es_primo es false, por lo que no se trata de un número primo
                break            #Termina la iteración
            i += 1               #Sumamos 1 para seguir mirando si el siguiente número i cumple con dicha condición
        if es_primo:             #Si es_primo (Se trata de un número primo)
            print(n)             #Imprima n
        n += 1                   #Sume uno y siga mirando si el siguiente número n es primo

if __name__ == "__main__":
    n = 2                        #Definimos n
    calcular_numeros_primos(n)



