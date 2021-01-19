"""
cpf = 168.995.350-09
"""

"""
cpf = '1 6 8 9 9 5 3 5 0'
cpf = cpf.split()
x = 10

if x >= 2:
    for i in cpf:
        print(i, x)
        x -= 1
"""


cpf = '43003804812'
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
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

if cpf == novo_cpf:
    print('Válido')
else:
    print('Inválido')












