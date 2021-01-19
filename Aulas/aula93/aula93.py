"""
Documentação.

Utilizamos o help() para mostrar o conteúdo da docStrings.
O docStrings, é para mostrar o que um determinado modulo faz.
"""
"""
import do
help(do)

"""
"""
Podemos utilizar DovStrings para nos referir as funções tambem.
"""
"""
typing - https://docs.python.org/3/library/typing.html
"""
x: int = 10
y: float = 2.34
z: bool = False


def funcao(p1: float, p2: int, p3: str) -> float:
    return 10.10


print(funcao(13.1, 20, 'Olá mundo'))

"""
from typing import Union

def funcao() -> Union[list, dict]  #Quer dizer que a função pode retornar 2 tipos
    return []
"""