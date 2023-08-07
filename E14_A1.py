"Escribir una función que calcule la media aritmética de una lista de números"
def mean(nums):
    #formula: x = (1+2+2+4+5+5+6) / 7 
    media = sum(nums, 0.0) / len(nums)
    return media

m = mean([1, 2, 2, 4, 5, 5, 6])
print("Resultado de la media aritmética: %s" %m)
