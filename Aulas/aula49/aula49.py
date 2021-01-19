"""

import sys

l1 = [x for x in range(10000)] #criando uma lista
l2 = (x for x in range(10000)) #criando um gerador

print(type(l1))
print(type(l2))

print(sys.getsizeof(l1)) #imprimindo o valor que esta sendo oculpado na memoria
print(sys.getsizeof(l2))
"""

#Criando um gerador.
def gera():
    for x in range(100):
        yield x


g = gera()

for y in g:
    print(y)











