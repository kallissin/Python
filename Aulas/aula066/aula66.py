import json
"""
w+ = apaga o que tem no arquivo e adiciona nova linha
a+ = acrescenta linha no arquivo, mantendo o conteudo original
r = faz apenas a leitura do arquivo
os.remove('abc.txt') = para apagar o arquivo.

file = open('abc.txt', 'w+')
file.write('Linha 1 \n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas: ')
print(file.read())
print('########')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('#######')
file.seek(0, 0)
for line in file.readlines():
    print(line, end='')
file.close()
"""
"""
try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
"""

"""
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0, 0)
    print(file.read())
"""
d1 = {
    'Pessoa 1': {
        'nome': 'Luis',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade' : 30,
    },
}

d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)

