" Crear un programa que genere una lista de números pares entre 1 y 100"
lista_pares = []
for i in range(1, 101):
    if i % 2 == 0:
        lista_pares.append(i)
print(lista_pares)
