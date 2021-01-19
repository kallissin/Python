"""

def calc(*args):
    list_int = list(*args)
    new_list = []
    cont1 = 0

    #Para a (nw_list) ter a mesma quantidade de sub-list que (list_int)
    while cont1 < len(list_int):
        new_list += [],
        cont1 += 1

    #Percorrer lista e valores das sub-listas
    cont = 0
    for x in list_int:
        temp = []
        for values in x:
            #Se existir valor DUPLICADO em (list_int), será adicionado a (nw_list)
            if values in temp and values not in new_list[cont]:
                new_list[cont].append(values)
            temp.append(values)
        #Se nas listas não existir valores duplicados, será retornado -1
        if len(new_list[cont]) == 0:
            new_list[cont].append(-1)
        cont += 1
    return new_list
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
"""

new_list = calc(lista_de_listas_de_inteiros)
print(new_list)
"""

def encontra_primeiro_duplicado(param_lista_de_inteiros):
    numeros_chegados = set()
    primeiro_duplicado = -1

    for numero in param_lista_de_inteiros:
        if numero in numeros_chegados:
            primeiro_duplicado = numero
            break
        numeros_chegados.add(numero)

    return primeiro_duplicado

for lista_de_inteiros in lista_de_listas_de_inteiros:
    print(encontra_primeiro_duplicado(lista_de_inteiros))





