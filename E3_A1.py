'Crear un programa que genere una lista de números aleatorios y los imprima en pantalla'
import random
lista = []
for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)
print(lista)
