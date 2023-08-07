"Escribir una función que calcule el factorial de un número dado"
n = int(input("Ingrese un numero: "))
factorial=1
if n!=0:
    for i in range(1,n+1):
        factorial=factorial*i
   
print("El factorial es: ",factorial)

  
