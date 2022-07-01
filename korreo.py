from cmath import log
from email.mime.text import MIMEText
from random import random
import smtplib

def send_correo(usuario,correo,cod):

    # ADMIN de correos
    gmail_admin = 'jeicob28@gmail.com'
    gmail_password = 'xuvmpuaeuqkzfden'
    sent_from = gmail_admin
    #code = random()
    code = cod
    # to = ['sierreitor17@gmail.com', 'jeicob28@yahoo.com']
    to = correo
    subject = 'OMG Super Important Message'

    html_template = f"""
                <h1>Geekflare</h1>

                <p>Hola {usuario},</p>
                <p>No su codigo de recuperacion de cuenta es el siguiente</p>
                <h3>{code}</h3>
                <p>No comparta con este codigo</p>
                """

    # html_content = MIMEText(html_template.format(usuario.split("@")[0]), 'html')
    html_content = MIMEText(html_template, 'html')


def send_info(usuario,correo,mensaje):

    # ADMIN de correos
    gmail_admin = 'jeicob28@gmail.com'
    gmail_password = 'xuvmpuaeuqkzfden'
    sent_from = gmail_admin
    #code = random()
    mj = mensaje
    # to = ['sierreitor17@gmail.com', 'jeicob28@yahoo.com']
    to = correo
    subject = 'Super Importante'

    html_template = f"""
                <h1>Geekflare</h1>

                <p>Hola {usuario},</p>
                <p>este correo es con fines informativos</p>
                <h3>{mj}</h3>
                <p>No responda este mensaje</p>
                """

    # html_content = MIMEText(html_template.format(usuario.split("@")[0]), 'html')
    html_content = MIMEText(html_template, 'html')

    try:
        print("CONECTANDO...")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print("Conectado check")
        server.ehlo()
        print("Loguendo...")
        server.login(gmail_admin, gmail_password)
        print("LOGUEADO")
        server.sendmail(sent_from, to,html_content.as_string(),)
        print("Correo enviado")
        server.close()
        print("Conexion cerrada")

        print ("Email sent!")
    except:
        print ("Algo malo ocurrio...")

#correo="jeicob28@yahoo.com"
#usuario="jeico"
#send_correo(usuario,correo)