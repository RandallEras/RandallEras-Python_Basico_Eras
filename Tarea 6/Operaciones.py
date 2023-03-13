#Calculadora

#def sumar():
    #nums = []
    #print("Ingresa la cantidad de numeros que quiera sumar")
    #n = int(input())
    #i = 0
    #while i < n:
        #print("Ingrese el valor: ", i + 1)
        #val = int(input())
        #nums.append(val)
        #i += 1
        #suma_nums = sum(nums)
    #print(suma_nums)        
    #return
    

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
        suma_nums = (lambda x: sum(x))(nums)  # Utilizando lambda para sumar los números
    print(suma_nums)        
    return

#En la línea 9, hemos utilizado una función lambda que toma una lista de números x como entrada y 
#devuelve su suma mediante la función incorporada "sum". 
#También hemos envuelto la función lambda en paréntesis y luego la hemos llamado con la lista nums para calcular la suma.


def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b


#def factorial(a):
    #resultado = a
    #for i in range(a-1,1,-1):
        #resultado = resultado * i
    #return resultado"""
    
def factorial(a):
    resultado = a
    for i in range(a-1,1,-1):
        resultado = resultado * i
    return resultado

numeros = [3, 4, 5, 6]  # lista de números para calcular el factorial

# Usando la función map() para aplicar la función factorial a cada número de la lista
fact = list(map(factorial, numeros))

print(fact)  
 

#def elevar_al_cubo(lista):
    #res = []
    #for item in lista:
        #res.append(item ** 3)
    #return res

#res = [2, 5, 6]
#resultado = elevar_al_cubo(res)
#print(resultado)

def potencia(base, exponente):
    return base ** exponente

base = [2, 3, 4, 5]
exponente = [2, 3, 4, 5]
resultados = list(map(potencia, base, exponente))
pares = list(filter(lambda x:x % 2 == 0, resultados))

print(resultados)
print(pares)

# Se ha definido la función potencia que toma dos argumentos, base y exponente, y devuelve
# el resultado de elevar la base a la potencia exponente.
# Se ha definido las listas base y exponente, y se utiliza map() para aplicar la función
# potencia a cada par de elementos de la lista base y exponente, obteniendo una lista de resultados.
# Finalmente se utiliza filter() y una función lambda para filtrar los resultados y obtener solo 
# los pares.


