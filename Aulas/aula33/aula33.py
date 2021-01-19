from random import randint
cpf = str(randint(100000000, 999999999))
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total += int(cpf[index]) * reverso
    reverso -= 1

    if reverso < 2:
        reverso = 11
        dig = 11 - (total % 11)

        if dig > 9:
            dig = 0
        total = 0
        cpf += str(dig)

print(f'Numero do CPF gerado: {cpf}')
