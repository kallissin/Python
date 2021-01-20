from string import Template
from datetime import datetime
from aula111.dados_email import minha_senha, meu_email

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

#ABRINDO E EDITANDO O TEMPLATE.
with open('template.html', 'r') as html:
    template = Template(html.read())
    date = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Anderson Felix', data=date)
    #podemos utilizar outro comando caso ouver no template "$outro" e não foi passado como argumento.
    #corpo_msg = template.safe_substitute(nome='Kelvin Alisson', data=date)

#CONFIGURANDO O EMAIL COM TITULO, REMETENDE E DESTINATARIO.
msg = MIMEMultipart()
msg['from'] = 'Joaozinho'  # Nome de quem esta enviando
msg['to'] = 'Joaozinho_inho_1233212@gmail.com'  # email de quem vai receber
msg['subject'] = 'Atenção: este é um e-mail de testes.'  # título do e-mail

#TEXTO DO EMAIL.
corpo = MIMEText(corpo_msg, 'html')

msg.attach(corpo)

#ENVIO DE IMAGEM EM ANEXO
with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

# CONECTANDO COM O SERVIDOR
# Se for hotmail, o "host" e "port" será diferente.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('Email não enviado...')
        print('Erro: ', e)
