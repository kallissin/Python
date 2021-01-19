"""
Dicionarios

no dicionário eu defino o valor do indice.
"""
"""
d1 = {'chave1':'valor da chave'} #criando um dicionario
d1 = dict(chave2='Valor da outra chave') #estou redefinindo o dicionario com novo valor
d1['nova_chave'] = 'valor da nova chave'  #adicionando valor ao dicionario
d1.pop(4) # irá excluir a chave que tem nome 4
d1.popitem() # irá excluir  ultimo item.
d1.update(d2) # colocando o dicionario2 no dicionario1
"""
"""
uma forma de encontrar valores no dicionario
print('str' in d1)  #checando chave
print('str' in d1.keys())  #checando chave
print('valor' in d1.values())  #checando valor

"""

"""
d1 = {
    'nome' : 'Kelvin',
    'sobrenome' : 'Alisson',
    'idade' : '25',
}

d1['trabalho'] = 'Analista'
d1.update({'nova_chave' : 'Novo valor'})  #adicionando valor a chave
del d1['idade']  #apagando a chave

if d1.get('nova_chave') is not None:  #verificando se existe essa chave
    print(d1.get('nova_chave'))
"""

d1 = {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3',
}
#for k in d1():          fazendo a busca da chave
#    print(k)

#for k in d1.values():        fazendo a busca dos valores
#    print(k)

#for k in d1.items():         fazendo a busca da chave e dos valores
#   print(k[0], k[1])

# for k, v in d1.items():     acessando a chave e o valor
#    print(k, v)

#for k in d1.items():          #fazendo a busca da chave e dos valores em tuplas
#    print(k)

clientes ={
    'cliente1' : {
        'nome' : 'Kelvin',
        'sobrenome' : 'Alisson',
    },
    'cliente2' : {
        'nome' : 'Maria',
        'sobrenome' : 'Silva',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

