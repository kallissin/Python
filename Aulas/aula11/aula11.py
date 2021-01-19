"""
Operadores Relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""
"""
var_1 = 'Kelvin'
var_2 = 'Cantarino'
expressao = var_1 == var_2

print(expressao)
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#idade para pegar emprestimo
menor_idade = 20
maior_idade = 30

if idade >= menor_idade and idade <= maior_idade:
    print(f"{nome} pode pegar o emprestimo.")
else:
    print(f'{nome} não pode pegar emprestimo.')

