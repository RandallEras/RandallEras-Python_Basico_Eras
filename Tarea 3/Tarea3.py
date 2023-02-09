
print ("\n *********Menu*********")

import Operaciones

def menucalculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. dividir")
    print("5. factorial")
    opcion= input("Escoja la operacion")
    

    if opcion == "1":
       resultado = Operaciones.sumar()
    if  opcion == "2":
        a = int(input("Ingresa un numero: "))
        b = int(input("Ingresa otro numero: ")) 
        resultado = Operaciones.restar(a, b)
    elif opcion == "3":
        resultado = Operaciones.multiplicar(a,b)
    elif opcion == "4":
        resultado = Operaciones.dividir(a,b)
        return resultado
    
    if opcion == "5":
        a = int(input("Ingresa un numero: "))
        resultado = Operaciones.factorial(a)
    return resultado
miresultado = menucalculadora()
print(miresultado)

archivo = open("Resultados.txt","w")
archivo.write("El resultado es:% s " %miresultado)

archivo.close()