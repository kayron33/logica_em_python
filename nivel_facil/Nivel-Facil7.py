#3. Quadrados de números
#Peça ao usuário para digitar um número N. Em seguida, use um laço for para imprimir o quadrado de todos os números de 1 até N.

print("Digite um numero")
n = int(input("Digite:> "))

for i in range(1,n + 1):
    print(f"{i} Elevado ao quadrado é: {i ** 2} ")