from calendar import mdays, monthrange

dia_semana, ultimo_dia = (monthrange(2020, 1))
"""
retorna uma tupla contendo o número do dia da semana (0-6)
0 - Segunda
1 - Terça
2 - Quarta
3 - Quinta
4 - Sexta
5 - Sabado
6 - Domingo

E retorna o ultimo dia do mes atual.
"""
print(dia_semana)
print(ultimo_dia)
