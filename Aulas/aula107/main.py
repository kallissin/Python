from aula107.dados import clientes_dicionario, clientes_json
import json

lista = [1,2,3,4,5,6]
#dados_json = json.dumps(clientes_dicionario, indent=4)
#print(dados_json)
"""
with open('Clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)

#Utilizamos para criar um arquivo json
"""


with open('Clientes.json', 'r') as file:
    dados = json.load(file)
#Utilizamos para ler um arquivo json e transformar em um dicionario
for key, values in dados.items():
    print(key, values)
