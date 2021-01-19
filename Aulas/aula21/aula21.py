frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_frase = ''
letra = input('Digite qual letra voce deseja colocar Maiúsculo: ')
while contador < tamanho_frase:
    if frase[contador] == letra:
        nova_frase += letra.upper()
    else:
        nova_frase += frase[contador]

    contador += 1
print(nova_frase)
