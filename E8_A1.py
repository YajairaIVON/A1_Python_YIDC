"Crear una función que invierta el orden de los elementos en una lista dada"
def invertir_orden(lista):
  lista.reverse()
  return lista

numeros = [99, 100, 101, 102, 103]
invertidos = invertir_orden(numeros)
print(invertidos) 
