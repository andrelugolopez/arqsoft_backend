import os
import sys
import html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from envio_correo import (cec,cen)
correo=cec
CodigoR=coR
usuario=cen
#credenciales
def email(usuario,correo,CodigoR):
  print(correo,usuario)
  proveedor_correo = 'smtp.live.com: 587'
  remitente = 'djmuthan@hotmail.com'
  password = '123jht987%'
  #conexion a servidor1
  servidor = smtplib.SMTP(proveedor_correo)
  servidor.starttls()
  servidor.ehlo()
  #autenticacion
  servidor.login(remitente, password)
  #mensaje 
  mensaje=f"""
  <html>
  <head>

  </head>

  <body>

  <table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
  <table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
      <tr>
        <td align="center">
          <p><a href=></a></p>
        </td>
      </tr>
    </table>

  <table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
      <tr>
        <td>
          <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="67C3F5">
            <tr>
              <td width="570" align="center"  bgcolor="#A2C3F5"><h1> Bienvenido 
              <br>{usuario, CodigoR}
            <br>  a tu Tienda ArqSoft</h1><br></td>
            </tr>
            <tr>
              <td width="570" align="right" bgcolor="#A2C3F5"><p>ArqSof</p></td>
            </tr>
          </table>
        </td>
      </tr>

      <tr>
        <td>
          <table id="content-3" cellpadding="0" cellspacing="0" align="center">
            <tr>
                <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="https://cdn.pixabay.com/photo/2016/03/26/13/09/cup-of-coffee-1280537_960_720.jpg" width ="250" height="150" />
              </td>
                <td width="15"></td>
              <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                  <img src="https://lh3.googleusercontent.com/10PWSmRo7NYH6pR5mIWJQwyzbSIG9IpMkvLMKm-brNetyJ6dh7f6BY3t5ePPhpIHdoJ-lOgBtE6sTXjtacTxdDFbp6Q1-vVf9OiyRDm2CGIe9fitoRKQEAUeU9VT7TkfiNVK1fsXQ7aVkGLrGsfUl4-yi6907Augjhj7pvBrUoOeoV_sZ8SLaeqiB3lZSGidk8Mc9e41cHsjucD1ANqBQuD0qF_FetF0Sam4wcv-zYjtlNTC50iriGO_twucj_vW7-0A7W44UL4yZYUR3AUebMx_x8TSB1m4EG_NSvzz-E8p9W17bKYVYr2lPzWBq-vd2T2Jw75htbs3xZPKDQ3LqVK4ho5NQTSH168k_ZxY8n7WEIoPXX2vPxkbTnwI1DXgrFa_-xdI7Yn11Q1MKNF2V-iLtYnMwYotodL-msmG2rsbYF6-UrQeq2c9k8bhnMg8c5DWpSwIoUj3Xxk2t3KJ2BM7Z8lSw8KzEeWCylSHuqhSF16H-1dIgXFiwsi-VjK6hWvz_05ThztfYsBLs9DSknfemyOP_mPBfmblP9r2sQZNRQKy04kv7kJuIKWVHte4pnhEdKSfqK_E0WLOkay0VJNAPOVtufvBtFsd1U0g5q9Tgh4JVs_5Yrx336RHGgWKUTfBU5Xo6fNXliim5hsTVKWNt1XbXu6hiGArpU4pcjW-laEou4TCQ5VP52Us6y0z9gQ5ezdPpov7iVRrNX1TxPSA=w162-h74-no?authuser=0" width ="250" height="150" />
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td>
          <table id="content-4" cellpadding="0" cellspacing="0" align="center">
            <tr>
              <td width="200" valign="top">
                <h4>Bienvenido Al Grupo Empresarial ArqSoft</h4>
                <p>En ArqSof, nos enorgullecemos de ofrecer a nuestros clientes un servicio receptivo, competente y excelente.</p>
              </td>
              <td width="15"></td>
              <td width="200" valign="top">
                <h4>Tienda ArqSoft</h4>
                <p>Nuestros clientes son la parte más importante de nuestro negocio, 
          y trabajamos incansablemente para garantizar su completa satisfacción, ahora y durante el tiempo que usted esté con nosotros.</p>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      

    </table>
    <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
      <tr>
        <td align="center">
          <p>ArqSoft Fábrica de Sueños Tecnológicos</p>
          </td>
      </tr>
    </table>
  </td></tr></table>

  </body>
  </html>
  """
  print(correo,usuario)
  msg = MIMEMultipart()
  msg.attach(MIMEText(mensaje,'html'))
  msg['From'] = remitente
  print(correo,usuario)
  msg['To'] = correo
  msg['Subject'] = 'Bienvenido a Tienda ArqSoft'
  servidor.sendmail(msg['From'] , msg['To'], msg.as_string())
  print ("correo enviado satisfactoriamente")
email(usuario,correo)