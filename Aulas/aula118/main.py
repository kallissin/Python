from time import sleep
from threading import Thread
from threading import Lock

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

t = MeuThread('Thread 1', 5)
t.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Ola mundo2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo3!', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo', 10))
t1.start()

#O que estiver em baixo de join, só sera executado assim que acabar o thread
t1.join()
while t1.is_alive():
    print('Esperando a Thread.')
    sleep(2)

print('Thread acabou!')
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print(f'não temos ingressos suficientes. Restam {self.estoque} em estoque')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Voce comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(9)

    threads = []
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False
        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)

    """
    
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(2)
    """
