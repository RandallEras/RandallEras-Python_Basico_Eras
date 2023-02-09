#Calculadora
def sumar():
    nums = []
    print("Ingresa la cantidad de numeros que quiera sumar")
    n = int(input())
    i = 0
    while i < n:
        print("Ingrese el valor: ", i + 1)
        val = int(input())
        nums.append(val)
        i += 1
        suma_nums = sum(nums)
    print(suma_nums)        
    return
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b
def factorial(a):
    resultado = a
    for i in range(a-1,1,-1):
        resultado = resultado * i
    return resultado
    