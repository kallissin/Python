"""
https://ffmpeg.zeranoe.com/builds/
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -SS 00:00:00 -to 00:00:10 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 18'  # (15 - 28) 18melhor qualidade e 28 a pior qualidade
preset = '-preset fast'  # (fast) arquivos menores
#codec_audio = '-c:a acc'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:02:30 -to 00:05:09'
#debug = ''

caminho_origem = r'C:\Users\kelvin\Videos\Entrada'
caminho_destino = r'C:\Users\kelvin\Videos\Saida'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)


        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):

            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'

        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{arquivo}_NOVO {extensao_arquivo}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf} {preset} {bitrate_audio} ' \
                  f'{debug} {map_legenda}"{arquivo_saida}"'

        os.system(comando)

