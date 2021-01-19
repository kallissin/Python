import random
import string
#Gera um numero inteiro entre A e B
#inteiro = random.randint(10, 20)

#gerar UM numero aleatorio usando a funcao range()
inteiro = random.randrange(900, 1000, 10)

#Gera um numero de ponto flutuante entre A e B
#flutuante = random.uniform(10, 20)

#Gera um numero de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Kelvin', 'Maria', 'Jose', 'Camila', 'Bartira', 'Danilo']

#irá sortear apenas um nome da lista
sorteio1 = random.choice(lista)
#irá sortear 2 nomes da lista, podendo repetir o mesmo nome
sorteio2 = random.choices(lista, k=2)
"""
#irá sortear 2 nomes da lista, porem, não irá repetir o nome

for i in range(100):
    sorteio3 = random.sample(lista, 2)
    print(sorteio3)

#embaralha a lista
random.shuffle(lista)
print(lista)
"""

#gera senha aleatória

letras = string.ascii_letters
digito = string.digits
caracteres = '!@#$%&*_-'
geral = letras + digito + caracteres


for i in range(100):
    senha = ''.join(random.choices(geral, k=8))
    print(senha)



