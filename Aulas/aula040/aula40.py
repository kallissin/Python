"""

lista = [
    ['P1', 13],
    ['P2', 50],
    ['P3', 25],
    ['P4', 7],
    ['P5', 23]
]

lista.sort(key=lambda item: item[1],reverse=True)
print(sorted(lista,key= lambda item: item[1], reverse=True))
"""

calculo = lambda x, y: x * y

print(calculo(10, 6))



