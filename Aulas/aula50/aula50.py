nome = 'Kelvin Alisson'
gerador = (x for x in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print('Aqui esta o restante do gerador consumido')

for letra in gerador:
    print(letra)
