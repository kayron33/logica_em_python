#1. Contagem de números
#Peça ao usuário para inserir um número e mostre todos os números de 1 até aquele número.

print("Me dê um numero que eu vou afzer a contagem")
num = int(input("Enviar:> "))

for i in range(1,num + 1):
    print(f"Conatgem {i}")