#Contar elementos

#Faça uma lista de números aleatórios.
#Conte quantos números são maiores que 10.

numeros = [10,10,0,11,12,13,14,15,16,17,18]
contador = 0 

for numero in numeros:
    if numero > 10:
        contador += 1
print(f"Essa é a quantidade de numeros maiores que 10:({contador})")
