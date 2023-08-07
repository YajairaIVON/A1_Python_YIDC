"Crear un programa que genere una matriz de números y la imprima en pantalla"
import random

def matriz(n):
  m = [[0] * n for _ in range(n)]
  for fila in range(n):
    for columna in range(fila, n):
      m[columna][fila] = m[fila][columna] = random.randint(0,100)
  return m

n = int(input("Ingrese el tamaño de la matriz: "))
matriz = matriz(n)
for fila in matriz:
  print(fila)
