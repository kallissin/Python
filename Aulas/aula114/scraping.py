# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup  # analizar o html e disponibilizar os dados
import csv

# Pegar a url e usar o request para manipular a url.
url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
# analizar o response e disponibinizar os dados.
html = BeautifulSoup(response.text, 'html.parser')
# criando uma lista com os dados coletados
lista = [(pergunta.select_one('.relativetime').text,
          pergunta.select_one('.question-hyperlink').text,
          pergunta.select_one('.vote-count-post strong').text
          ) for pergunta in html.select('.question-summary')]

# criando um arquivo csv
with open('arquivo.csv', 'w') as file:
    escrever = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    escrever.writerow(
        [
            "Data",
            "Titulo",
            "Votos"
        ]
    )
    for dados in lista:
        escrever.writerow(
            [dados]
        )
