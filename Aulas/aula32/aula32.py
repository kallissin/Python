cpf = '16899535009'
novo_cpf = cpf[:-2]
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso
    reverso -= 1

    if reverso < 2:
        reverso = 11
        dig = 11 - (total % 11)

        if dig > 9:
            dig = 0
        total = 0
        novo_cpf += str(dig)

if novo_cpf == cpf:
    print('Válido')
else:
    print('Inválido')

