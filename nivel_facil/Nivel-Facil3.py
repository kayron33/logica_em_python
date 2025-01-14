#Tabuada
#Crie um programa que gere a tabuada de um número fornecido pelo usuário.
#Exemplo: Para o número 5, o programa deve imprimir:

while True:
   print("Digite o numero")
   num = int(input("Enviar:> "))
   for i in range(1,11):
      print(f"{num} X {i} = {num * i}")


