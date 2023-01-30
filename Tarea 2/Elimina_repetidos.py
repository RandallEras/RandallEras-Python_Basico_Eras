#eliminar elementos repetidos de una lista

lista = [1, 2, 3, 2, 3, 5, 6, 3, 2, 5]
conjunto = set(lista)
lista = list(conjunto)
print(lista)