"Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no"
import re

def palindromo(cadena):
  cadena = cadena.lower()
  cadena = re.sub("[^a-záéíóúüñ]", "", cadena)
  return cadena == cadena[::-1]

frase = input("Ingresa una cadena de texto: ")
es_palindromo = palindromo(frase)
if es_palindromo:
  print("La cadena es un palíndromo")
else:
  print("La cadena no es un palíndromo")
