n = 0
i = int(input("ingrese un número natural entre 2 y 50: "))

while n<=i:
  n+=1
  if i%n==0 and i!=0 and i!=1 and i<50:
    print(n, end=",")

if i == 0 or i==1:
  print("Ingrese un número mayor o igual a dos ")
elif i >50:
  print("Ingrese un menor o igual a cincuenta ")
  
print(" son los divisores de " + str(i))