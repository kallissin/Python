"""
documentação:
https://pythonhosted.org/PyPDF2/PdfFileReader.html
exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
pip install pypdf2
pipenv install pypdf2
"""
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os

"""
#juntar arquivos
caminho_dos_pdfs = 'pdf1'

novo_pdf = PdfFileMerger()


for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        new = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(new)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""
#dividir arquivos por paginas, caso desejar juntar as paginas, poderá utilizar o codigo a cima.
with open('pdf1/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'ab') as novo_pdf:
            escritor.write(novo_pdf)
        