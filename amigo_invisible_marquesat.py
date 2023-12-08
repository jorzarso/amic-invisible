import numpy as np
from email.message import EmailMessage
import smtplib

participant1 = 'Jose Maria'
participant2 = 'Sali'
participant3 = 'Paco'
participant4 = 'Ade'
participant5 = 'Jose'
participant6 = 'Gemma'
participant7 = 'Marta'
participant9 = 'Belén'
participant8 = 'Jorge'

restricciones = {}

lista_participantes = ['Jose Maria', 'Sali', 'Paco', 'Ade', 'Jose', 'Gemma', 'Marta', 'Jorge', 'Belén']
cantidad_participantes = len(lista_participantes)

eleccion = np.random.permutation(lista_participantes)
while any(x == y or y in restricciones.get(x, []) for x, y in zip(lista_participantes, eleccion)):
    eleccion = np.random.permutation(lista_participantes)

eleccion = eleccion.tolist()

remitente = "jorzarso1989@gmail.com"
correo = ["depradas57@gmail.com", "mariajuanrosalia@gmail.com", "pacocarrillo12200@gmail.com", "adegballester@gmail.com", "jluisalfaro1989@gmail.com", "gemmacalpemaria@gmail.com", "cgmartaa@gmail.com", "jorzarso1989@gmail.com", "beleninsnoo@gmail.com"]

lista_participantes2 = ['Jose Maria', 'Sali', 'Paco', 'Ade', 'Jose', 'Gemma', 'Marta', 'Jorge', 'Belén']
for i in lista_participantes2:
    indice = lista_participantes2.index(i)
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = correo[indice]
    email["Subject"] = "Amic invisible"

    # Crear el contenido del correo en formato HTML con CSS y huellas de perros
    contenido_html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f9f9f9;
            }}
            .container {{
                margin: 20px;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                position: relative;
            }}
            h1 {{
                color: #333333;
            }}
            p {{
                color: #555555;
            }}
            .dog-paw {{
                width: 30px;
                height: 30px;
                display: inline-block;
                position: absolute;
            }}
            .paw-1 {{
                top: 20px;
                left: 20px;
            }}
            .paw-2 {{
                top: 60px;
                left: 50px;
            }}
            /* Agrega más clases de huellas según sea necesario */
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Amigo Invisible!</h1>
            <p>Hola {i},</p>
            <p>Vas a ser l'amic invisible de: {eleccion[indice]}</p>
            <p>¡Contesta al correu per a confirmar que l'has rebut!</p>
            <img class="dog-paw paw-1" src="huella-perro1.png" alt="Dog Paw">
            <img class="dog-paw paw-2" src="perro.png" alt="Dog Paw">
            <!-- Agrega más imágenes de huellas de perros según sea necesario -->
        </div>
    </body>
    </html>
    """

    email.add_alternative(contenido_html, subtype='html')  # Agregar el contenido HTML como alternativa

    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    # Password extra: gmail->seguridad->contraseñas de aplicaciones->Otra->Python->it must be put the password given by google
    # change knbn iuol fmrk ocbs for the password commented
    smtp.login(remitente, "knbn iuol fmrk ocbs")
    smtp.sendmail(remitente, correo[indice], email.as_string())
    smtp.quit()
