from datetime import datetime
from locale import LC_ALL, setlocale, getlocale, LC_TIME


def _getlang():
    # Descubra como o idioma atual está definido
    return getlocale(LC_TIME)


print(_getlang())
setlocale(LC_ALL, '')

# quarta 13 de janeiro de 2021
date = datetime.now()
formatacao1 = date.strftime('%H:%M:%S')
formatacao2 = date.strftime('%A %w de %B de %Y')
print(formatacao1)
print(formatacao2)

with open('../aula103/horas.txt', 'w') as file:
    file.write(f'Data: {formatacao2}\n'
               f'Horas: {formatacao1}')
