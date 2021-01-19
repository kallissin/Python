"""
Comma Separated Value - CSV (Valores separados por vírgula)
É um formatado de dados muito usado em tabelas (Excel, Google Sheets),
bases de dados, clietes de e-mail, etc..
"""
import csv

with open('clientes.csv', 'r') as file:
    dados = [x for x in csv.DictReader(file)] #ou podemos utilizar somente Reader

#criando um novo arquivo.
with open('clientes2.csv', 'w') as file:
    #modelando o nosso arquivo com delimitador, etc.
    escreve = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    #pegando as chaves do dicionario e colocando em uma lista.
    chaves = dados[0].keys()
    chaves = list(chaves)
    #escrevendo as chaves da lista no arquivo.
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )
    #percorrendo os valores da lista e escrevendo no arquivo
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
