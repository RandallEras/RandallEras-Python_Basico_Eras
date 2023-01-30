#Calcular el factorial de un numero dado
num = int(input("Ingrese un número: "))
factorial = 1
if num > 0:
    for i in range(1, num+1):
        factorial = factorial * i
    print ("El factorial de ",num, "es: ",factorial)
else: 
    print("ERROR! A ingresado un número menor a 1")