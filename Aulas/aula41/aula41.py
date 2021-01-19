t1 = (1, 2, 3, 'Kelvin', 'João')

for n in t1:
    print(n)

n1, n2, n3, *_ = t1

print(n3)