#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% 
#respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
#A--> 25 MILLONES
#B -->18.9

año: int = 2022
A : float = 25
B : float = 18.9
while B<=A:
    A+= (0.02*A) 
    B+= (0.03*B)
    año+=1

print("Para el año " + str(año)  +  " la población B superará a la población A")
