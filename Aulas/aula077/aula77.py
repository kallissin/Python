class A:
    vc = 123


a1 = A()
a2 = A()
A.vc = 321  # utilizamos desta forma para alterar o valor da variavel.
# a1.vc = 321 Não utilizamos desta forma para alterar o valor da variavel vc
print(a1.vc)
print(a2.vc)
print(A.vc)
