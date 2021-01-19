from aula79.classe import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Kelvin')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
