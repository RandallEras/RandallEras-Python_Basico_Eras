def secuencia (valores):
    val = valores
    dic = {}
    dicfinal = {}
    lista = []
    for letra in val:
        if letra in dic:
            dic [letra] += 1
        else:
            dic[letra] = 1
            
    lista = dic
    
    return lista



valores = input ("Ingrese una palabra")
secuencia (valores)

print (secuencia(valores))

