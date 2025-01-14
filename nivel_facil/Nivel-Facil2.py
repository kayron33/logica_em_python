#Soma de Números
#Receba vários números do usuário até que ele digite "0". Depois, exiba a soma de todos os números inseridos.

soma = 0

while True:
    print("Digite o numero")
    num = int(input('Enviar:>'))

    if num == 0:
        break
    soma += num

print(f"O resultado da soma é : {soma}")