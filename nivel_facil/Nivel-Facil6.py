#3. Multiplicação de números até 10
#Peça ao usuário para digitar um número e mostre a multiplicação dele com os números de 1 a 10.

print ("Digite o valor para calculadora")
numero = int(input('Enviar:> '))

for i in range(1,11):
    print(f"{numero} X {i} = {numero * i}")