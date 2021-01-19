from aula71.cnpj import remove_caractere, remove_digit, values

cnpj = '40.688.134/0001-61'
cnpj_original = remove_caractere(cnpj)
cnpj = remove_digit(cnpj_original)

values(cnpj, cnpj_original)


