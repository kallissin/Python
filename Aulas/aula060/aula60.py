try:
    a = 0
    try:
        a = 1/0
    except:
        print('erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = ''