from aula70.calcular.number import convert
"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa.
    listar terefas.
    opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação.)
    opção de refazer(a cada vez que chamarmos, refaz a ultima ação.)
"""
print('*' * 16)
print('Lista de tarefas')
print('*' * 16)
print()

lista = []
lista_temporario = []
valor_temporario = ''
valor = 1

while valor != 0:
    print('[1] - Nova tarefa \n'
          '[2] - Listar tarefas \n'
          '[3] - Desfazer tarefa \n'
          '[4] - refazer tarefa \n'
          '[0] - Sair\n')
    valor = input('Digite um valor CORRESPONDENTE: ')

    valor = convert(valor)

    if valor == 1:
        vl = (input('Digite a nova tarefa: '))
        lista.append(vl)
    elif valor == 2:
        print('*****TAREFAS*****')
        print(f'{lista}\n')
    elif valor == 3:
        lista_temporario.append(lista.pop())
    elif valor == 4:
        if len(lista_temporario) > 0:
            valor_temporario = lista_temporario.pop()
            lista.append(valor_temporario)

