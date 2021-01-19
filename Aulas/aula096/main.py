from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple

@dataclass(eq=True, repr=True, frozen=False, order=True, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    #@property
    #def nome_completo(self):
    #    return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('A', '5')
p2 = Pessoa('B', '3')
p3 = Pessoa('C', '4')
p4 = Pessoa('D', '6')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome))

#print(p1 == p2)

print(asdict(p1))
print(astuple(p2))
