from dados import produtos, pessoas, lista
"""
nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]
print(lista)
print(list(nova_lista))
"""
"""
def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.5, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produtos in novos_produtos:
    print(produtos)
"""

lista_pessoas = map(lambda p: p['nome'], pessoas)

print(list(lista_pessoas))