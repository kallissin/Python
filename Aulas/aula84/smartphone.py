from aula84.eletronico import Eletronico
from aula84.log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} Já está conectado'
            print(error)
            self.log_error(error)
            return

        else:
            self._conectado = True
            info = f'{self._nome} está conectado'
            print(info)
            self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            error = f'{self.nome} Não está conectado'
            print(error)
            self.log_error(error)
            return
        self._conectado = False
        info = f'{self._nome} Desconectado com sucesso'
        print(info)
        self.log_info(info)
