from aula81.classe import Cliente, Endereco

cliente1 = Cliente('Luis', 20)
cliente1.inseri_endereco('Franca', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 53)
cliente2.inseri_endereco('São Salvador', 'BA')
cliente2.inseri_endereco('Belo Horizonte', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 23)
cliente3.inseri_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()
print('################################################')

