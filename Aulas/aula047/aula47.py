string = '012345678901234567890123456789012345678901234567890123456789'
m = 10
lista = [string[i: i + m] for i in range(0, len(string), m)]
retorno = '.'.join(lista)
print(lista)
print(retorno)

