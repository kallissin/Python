from PyPDF2 import PdfFileReader, PdfFileWriter


def dividir_arquivos():
    # dividir arquivos por paginas
    with open('pdf1/novo_arquivo.pdf', 'rb') as arquivo_pdf:
        leitor = PdfFileReader(arquivo_pdf)
        num_paginas = leitor.getNumPages()

        for num_pagina in range(num_paginas):
            escritor = PdfFileWriter()
            pagina_atual = leitor.getPage(num_pagina)
            escritor.addPage(pagina_atual)

            with open(f'novos_pdfs/{num_pagina}.pdf', 'ab') as novo_pdf:
                escritor.write(novo_pdf)