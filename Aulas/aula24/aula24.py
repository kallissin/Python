nome = ['Kelvin Cantarino', 'Bartira Faria', 'Jose augusto']
nome_j = False

for valor in nome:
    if valor.lower().startswith('j'):
        nome_j = True

if nome_j:
    print('Esse nome tem a letra "J" ')
else:
    print('Esse nome não tem a letra "J" ')

