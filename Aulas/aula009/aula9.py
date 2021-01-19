"""
Entrada de dados
"""
nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
ano_nasc = 2020 - int(idade)

print()
print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nasc}.')

#print(f'O usuário digitou {nome} e o tipo da variavel é '
 #     f'{type(nome)}')
