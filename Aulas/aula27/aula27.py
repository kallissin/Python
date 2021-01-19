x = 10
y = 'Luis'
"""
m = x
x = y
y = m
"""

print(x, y)

# No python podemos fazer de uma maneira mais simples que não necessita de uma
# terceira variavel.
x, y = y, x
print(x, y)
