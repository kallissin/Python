"""
Faça um programa que peça ao usuário para digitar um numero inteiro.
Informe se estu número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
n1 = input("Digite um número inteiro: ")

if n1.isdigit():
    n1 = int(n1)
    
    if n1 % 2 == 0:
        print(f'{n1} é um número PAR')
    else:
        print(f'{n1} é um número IMPAR')
else:
    print('Por favor, digite um número inteiro')
"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
horario = input("Digite um horario (0-23): ")

if horario.isnumeric():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Por favor, digite um horário entre 0 e 23.')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Digite um horário entre 0 e 23')
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite o seu primeiro nome: ')
qtd_letras = len(nome)

if qtd_letras <= 4:
    print('Seu nome é curto')
elif qtd_letras >= 5 and qtd_letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
