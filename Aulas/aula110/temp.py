from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    date = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Kelvin Alisson', data=date)
    #podemos utilizar outro comando caso ouver no template "$outro" e não foi passado como argumento.
    #corpo_msg = template.safe_substitute(nome='Kelvin Alisson', data=date)

print(corpo_msg)