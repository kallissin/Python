"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
novo_texto = ''
for n in texto:
    if n == 't':
        continue
        novo_texto += n.upper()
    else:
        novo_texto += n
print(novo_texto)

