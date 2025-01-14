# escrevendo o algoritimo 
#o programa deve repetir até a pessoa clicar para sair 
while True:
    print("Escreva (sair) para sair do programa")
    op = input('Deseja continuar?')
    if op.lower == "sair":
        print("Saindo")
        break
    #programa deve receber um numero
    num = int(input("Digite um numero"))

    
# Falar se é impar ou par
    if op.lower == "continuar":
        if num % 2 == 0:
            print(f"O numero {num} é par")
        else:
            print(f"O numero{num} é impar ")

        




