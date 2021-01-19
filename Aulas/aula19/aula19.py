"""
while em python
utilizado para realizar ações enquanto
uma condição for verdadeira.
"""
#continue serve para pular uma determinada linha de codigo, alem disso,
#ele volta para o inicio da estrutura de repetição.
#break serve para parar o código, ele interrompe. finalizando o loop

x = 0  # coluna
"""

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'x vale {x} e y vale {y}')
        y += 1

    x += 1
"""

while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digite um operador [+][-][/][*] ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Digitar um numero inteiro...')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        print('Operador Inválido')

    sair = input('Deseja continuar? [s]im , [n]ão: ')
    if sair == 'n':
        break
