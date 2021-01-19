def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

numero = converte_numero(input('Digite um numero: '))

if numero is not None:
    print(numero + 5)
else:
    print('Isso não é um numero')