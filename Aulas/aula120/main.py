"""
pilhas e filas
pilha (stack) - LIFO - last in, first out
"""
"""
# pilha
livros = list()
livros.append('Livro 1')  # 1
livros.append('Livro 2')  # 2
livros.append('Livro 3')  # 3
livros.append('Livro 4')  # 4
livros.append('Livro 5')  # 5
livro_removido = livros.pop()  # 5
livro_removido = livros.pop()  # 4
livro_removido = livros.pop()  # 3
livro_removido = livros.pop()  # 2
livro_removido = livros.pop()  # 1

print(livros, livro_removido)
"""

from collections import deque
from time import sleep

"""
# fila
#para tirar o primeiro elemento podemos utilizar tambem o fila.popleft()
fila = deque(maxlen=10)

for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)
"""
fila = deque(maxlen=10)
fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#fila.insert(2, 'Kelvin Cantarino')  # se a fila estiver cheia não tem como inserir

fila.remove(2)
print(fila)
