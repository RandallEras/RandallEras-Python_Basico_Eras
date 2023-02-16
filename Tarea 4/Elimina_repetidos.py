#Eliminar elementos repetidos de dos listas

lista1 = [1, 2, 3, 2, 3, 5, 6, 3, 2, 5]
lista2 = ["gato", "gato", "sombrero", "gato", "zanahoria"]
result = []
for item in (lista1, lista2):
    for item in item:
        if item not in result and not (item  in lista1 and item  in lista2):
            result.append(item)       
        result
print(result)
