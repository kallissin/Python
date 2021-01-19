from itertools import groupby

alunos = [
    {'Nome':'Kelvin','Nota':'A'},
    {'Nome':'Bartira','Nota':'B'},
    {'Nome':'Joana','Nota':'A'},
    {'Nome':'Karine','Nota':'C'},
    {'Nome':'Leticia','Nota':'D'},
    {'Nome':'Eduardo','Nota':'A'},
    {'Nome':'João','Nota':'B'},
    {'Nome':'Alexandre','Nota':'A'},
    {'Nome':'Antonio','Nota':'C'},
    {'Nome':'Camila','Nota':'B'},
]
ordena = lambda item: item['Nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
quant_aluno = 0

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    for aluno in valores_agrupados:
        print(f'\t{aluno}')
        quant_aluno += 1

    print(f'\t{quant_aluno} alunos tiraram nota {agrupamento}')
    print()
    quant_aluno = 0
