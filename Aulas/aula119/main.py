#documentação:
#https://pythonhosted.org/PyPDF2/PdfFileReader.html

#exemplos de uso:
#http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

#pip install pypdf2
#pipenv install pypdf2
from aula119.compactar import juntar_arquivos
from aula119.descompactar import dividir_arquivos

if __name__ == '__main__':
    juntar_arquivos()  # Caso for utilizar a outra função, não esqueça de comentar essa.
    #dividir_arquivos()