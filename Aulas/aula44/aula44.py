"""
sets, só suporta elementos imutaveis.
ele não aceita elementos duplicados.
"""
#add (adiciona), update (atualiza), clear, discard
#union | (une)
#intersection & (todos os elementos presentes nos dois sets)
#difference - (elementos apenas no set da esquerda)
#symmetric_difference ^ (elementos que estao nos dois sets, mas não em ambos)
"""
s1 = {1, 2, 3, 4, 5}
print(s1, type(s1))
"""
"""
s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)
print(s1)
"""
"""
s1 = set()
s1.update('python')
print(s1)
"""

"""
é possivel pegar uma lista com elementos duplicados e fazer o casting para set,
com isso seria eliminado os elementos duplicados. depois é só fazer outro casting.
"""
"""

l1 = [1, 2, 5, 6, 2, 7, 8, 4, 2, 7, 4, 5, 2, 1]
l1 = set(l1)
l1 = list(l1)
print(l1, type(l1))

"""

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 & s2

print(s3)






