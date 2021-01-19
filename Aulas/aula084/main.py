"""

class A:
    def falar(self):
        print('Falando... estou em A')

class B(A):
    def falar(self):
        print('Falando... estou em B')

class C(A):
    def falar(self):
        print('Falando... estou em C')

class D(B, C):
    def falar(self):
        print('Falando... estou em D')

d = D()
d.falar()
"""
from aula84.smartphone import Smartphone

smartphone = Smartphone('Samsung')
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.desconectar()
smartphone.desligar()


