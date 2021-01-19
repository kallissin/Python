from dados import pessoas, produtos, lista
"""
nova_lista = filter(lambda p: p['preco'] > 50, produtos)

for produto in nova_lista:
    print(produto)
"""
def year(idade):
    if idade['idade'] > 18:
        return True
    else:
        return False

nova_lista = filter(year, pessoas)

for idade in nova_lista:
    print(idade)
