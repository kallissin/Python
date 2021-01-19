#import vendas.cal_preco
#from vendas import cal_preco
from aula65.vendas.cal_preco import aumento, reducao
from aula65.vendas.formata import preco as formata
preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)

print(formata.real(50))