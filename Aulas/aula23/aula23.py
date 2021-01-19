"""
Listas
fatiamento
append, insert pop, del, clear, extend, +
min, max
range
"""
"""
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 8, 9, 10]
l3 = l1 + l2
l4 = list(range(1, 10))
l1.extend(l2)  # acrescenta a lista l2 na lista l1.
l2.append('b')  # adiciona um valor no fim da lista.
l2.insert(0, 'banana')  # adiciona valor banana no indice 0 da lista
l2.pop()  # exclui o ultimo  item da lista.
del(l2[3:5])  # exclui os itens do indide 3 e 4 porque o 5 não conta.

for valor in l2:
    print(valor)
"""
"""
1º escolher a palavra secreta
2º verificar se o usuário digitou mais de uma letra
3º o que o usuário digitar precisa ficar armazanado em uma lista.
4º se a letra que o usuário digitou não estiver na palavra secreta,
ela deverá ser excluida da lista.
5º criar um laço FOR. para verificar o que o usuário digitou esta 
na palavra chave e se tiver deverá ser colocado em uma variavel,
omitindo o restante das letrar.
6º criar uma forma de o usuário ter apenas 3 chances.
"""
secreto = 'comida'
digitadas = []
chance = 3

while True:
    print('')
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ooohol. Isso não vale. Digite APENAS uma letra.')
        continue

    digitadas.append(letra)

    if not letra in secreto:
        if chance >= 1:
            print(f'A letra "{letra}" NÃO EXISTE. Você tem só mais {chance} chance.')
            chance -= 1
            digitadas.pop()
        elif chance == 0:
            print(f'A letra "{letra}" NÃO EXISTE. As suas chances acabaram.')
            print('##############')
            print('Voce Perdeu!!!')
            print('##############')
            break

    secreto_temporario = ''
    for x in secreto:
        if x in digitadas:
            secreto_temporario += x
        else:
            secreto_temporario += '*'

    if letra in secreto:
        print(f'Existe a letra "{letra}" na palavra secreta.')


    if secreto_temporario == secreto:
        print('PARABENS!!!!!! VOCÊ GANHOU!!!!!')
        print(f'A palavra secreta é "{secreto}"')
        break
    else:
        print(f'Palavra secreta {secreto_temporario}')



