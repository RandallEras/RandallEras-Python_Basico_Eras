#Programa que indica la cantidad de letras, números y simbolos de una cadena.

def tipoDatos (cadena):
    num=0
    lista_num=[]
    let=0
    lista_letras=[]
    simb=0
    lista_simb=[]
    for i in cadena:
        n= i.isdigit()
        c=i.isalpha()
        if n == True:
            num +=1
        elif c == True:
            let +=1
        elif n== False and c== False:
            simb +=1
    return num,let,simb
        

cadena= input("Digite los caracteres: ")
nume,letr,simbol= tipoDatos(cadena)
print("La cadena tiene ", nume, " números, ", letr, "letras y ", simbol, "símbolos")


