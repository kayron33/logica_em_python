# 2. Verificando maioridade
#Peça ao usuário para inserir a idade e diga se ele é maior de idade (18 anos ou mais) ou menor.

print("digite a sua idade")
idade = int(input('Enviar:> '))
if idade < 18:
    print(f"Você tem {idade}, e logo você é menor de idade")
elif idade >= 18:
    print(f"Sua idade é {idade}, logo você já é maior de idade")

