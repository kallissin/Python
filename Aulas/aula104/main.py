import os
from aula104.me_encontra import formata_tamanho


caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')


cont = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                cont += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Você não tem permissão para abrir este arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido:', e)

print()
print(f'{cont} arquivo(s) encontrado(s)')
