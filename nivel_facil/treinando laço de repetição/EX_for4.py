#Contagem regressiva
#Exiba uma contagem regressiva de 10 a 0, incluindo uma mensagem de "Lançamento!" ao final.

print("Diga um numero")
num = int(input("Enviar:> "))

for i in range(num,-1,-1):
    print(i)