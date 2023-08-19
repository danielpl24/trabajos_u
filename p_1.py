#Crea un algoritmo para calcular el promedio de tres números ingresados por el usuario.
print("calculador de promedio de tres nmumeros")
#suma de los numeros divido en la cantidad de numeros = promedio
p=[]
for i in range(3):
    x=int(input("ingresa el numero"))
    p+=[x]
promedio=(p[0]+p[1]+p[2])/3
print("el promedio es:",promedio,"los numeros ingresados fueron:",p)
