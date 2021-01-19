"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
def saudacao(saudacao, nome):
    print(saudacao, nome)

saudacao('Bom dia', 'Kelvin')
"""

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

def calcular(n1, n2, n3):
    total = n1 + n2 + n3
    print(f'O valor da soma entre {n1} + {n2} + {n3} = {total}')
calcular(10, 7, 3)
"""

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro somado do aumento 
do percentual do mesmo.

def calcular(valor, perc):
    valor += (valor * (perc / 100))
    return valor

total = calcular(150, 10)
print(f'O valor calculado é {total}')
"""

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parametro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divísivel por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado. 
"""

def calcular(valor):

    if valor % 3 == 0 and valor % 5 == 0:
        return f'FizzBuzz'
    if valor % 3 == 0:
        return f'Fizz'
    if valor % 5 == 0:
        return f'Buzz'
    return valor

num = int(input('Digite um número: '))
valor = calcular(num)
print(valor)
