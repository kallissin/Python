from PyPDF2 import PdfFileMerger
import os

# O código a baixo irá juntar arquivos em PDF
def juntar_arquivos():
    caminho_dos_pdfs = 'pdf1'

    novo_pdf = PdfFileMerger()

    for root, dirs, files in os.walk(caminho_dos_pdfs):
        for file in files:
            caminho_completo_arquivo = os.path.join(root, file)
            new = open(caminho_completo_arquivo, 'rb')
            novo_pdf.append(new)

    with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
        novo_pdf.write(meu_novo_pdf)
