import re


def remove_caractere(cnpj):
    cnpj = re.sub(r'[^0-9]', '', cnpj)
    return cnpj


def remove_digit(cnpj):
    cnpj = cnpj[:-2]
    return cnpj


def values(cnpj, cnpj_original):
    cnpj = first_digit(cnpj)
    novo_cnpj = last_digit(cnpj)
    checker_cnpj(novo_cnpj, cnpj_original)


def first_digit(cnpj):
    k = 5
    calculo = 0
    for v in cnpj:
        calculo += int(v) * int(k)
        k -= 1
        if k < 2:
            k = 9
    digt1 = 11 - (calculo % 11)
    if digt1 > 9:
        digt1 = 0
    cnpj += str(digt1)
    return cnpj


def last_digit(cnpj):
    k = 6
    calculo = 0
    for v in cnpj:
        calculo += int(v) * int(k)
        k -= 1
        if k < 2:
            k = 9
    digt2 = 11 - (calculo % 11)
    if digt2 > 9:
        digt2 = 0
    cnpj += str(digt2)
    return cnpj


def checker_cnpj(novo_cnpj, cnpj_original):
    if novo_cnpj == cnpj_original:
        print('CNPJ Válido')
    else:
        print('CNPJ Inválido')

