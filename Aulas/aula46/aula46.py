l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex1 = [variavel for variavel in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v, vl) for v in l1 for vl in range(3)]

l2 = ['Kelvin', 'Maria', 'Bartira']

ex4 = [v.replace('a', '@').upper() for v in l2]

tupla =(
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(y, x) for x, y in tupla]

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else '0' for v in l3]

print(ex1)
print(ex2)
print(ex3)
print(ex4)
print(ex5)
print(ex7)