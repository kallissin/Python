from zipfile import ZipFile
import os

# caminho da pasta
caminho = r'C:\pasta teste\dados_json'

# Compactando o arquivo que estiver na pasta a cima
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

# Fazendo a leitura do arquivo que estiver na pasta zipada
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Descompactando o "arquivo.zip" na pasta descompactado
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')