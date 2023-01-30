def intercalar(palabra_a, palabra_b):

    r = " "
    i = 0
    l = len(palabra_a)

    while i < l:
        print(palabra_a[i] + palabra_b[i], end = "")
        i = i + 1
    return r

a = input("Ingrese palabra a: ") 
b = input("Ingrese palabra b: ")



if len(a)==len(b):
    cambiar = intercalar(a, b)
    print(cambiar)
else:
    print(" Error")