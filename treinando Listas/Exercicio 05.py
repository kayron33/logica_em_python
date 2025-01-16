numeros = [34, 12, 5, 23, 8]

# Usando sort() com reverse=True para ordem decrescente
numeros.sort(reverse=True)
print(f"Lista ordenada (decrescente) com sort(): {numeros}")

# Usando sorted() com reverse=True para uma nova lista
nova_lista = sorted(numeros, reverse=True)
print(f"Nova lista ordenada (decrescente) com sorted(): {nova_lista}")

# Usando sort() para alterar a lista original
numeros.sort()
print(f"Lista ordenada (crescente) com sort(): {numeros}")

# Usando sorted() para obter uma nova lista ordenada
nova_lista = sorted(numeros)
print(f"Nova lista ordenada (crescente) com sorted(): {nova_lista}")