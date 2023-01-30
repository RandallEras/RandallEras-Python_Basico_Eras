# Triangulo de numeros consecutivos 
num = int(input("Ingrese un número: "))
if num < 1:
    print ("A ingresado un número no permitido")
else:
    filasn = ""
    for i in range(1,num + 1):
        filasn = "".join([filasn,str(i)])
        print(filasn)           