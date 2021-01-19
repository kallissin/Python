
lista_a = [1, 2, 3, 4]
lista_b = [1, 2, 3, 4, 5, 6]
"""
nova_lista = []
for i in range(len(lista_a)):
    nova_lista.append(lista_a[i] + lista_b[i])
print(nova_lista)
"""
nova_lista = [x + y for x, y in zip(lista_a, lista_b)]
print(nova_lista)