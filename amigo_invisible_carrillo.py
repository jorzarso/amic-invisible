import numpy as np
from numpy.core.defchararray import index 
from email.message import EmailMessage
import smtplib

participant1 = 'Abuelo'
participant2 = 'Abuela'
participant3 = 'Vicente'
participant4 = 'Rosa'
participant5 = 'Carlos'
participant6 = 'Anna'
participant7 = 'Luis'
participant8 = 'Raquel'
participant9 = 'Jorge'
participant10 = 'Belén'

restricciones = {
    participant1: [participant2],
    participant2: [participant1],
    participant3: [participant4],
    participant4: [participant3],
    participant5: [participant6],
    participant6: [participant5],
    participant7: [participant8],
    participant8: [participant7],
    participant9: [participant10],
    participant10: [participant9]
}

lista_participantes = ['Abuelo','Abuela','Vicente','Rosa','Carlos','Anna','Luis','Raquel','Jorge','Belén']
cantidad_participantes=len(lista_participantes)

    
eleccion = np.random.permutation(lista_participantes)
while any(x == y or y in restricciones.get(x, []) for x, y in zip(lista_participantes, eleccion)):
    eleccion = np.random.permutation(lista_participantes)

eleccion = eleccion.tolist()

remitente = "jorzarso1989@gmail.com"
correo=["viczarbo@gmail.com","mariasorolla48@gmail.com","viczarzoso@gmail.com","rosamariagrso74@gmail.com","zarzosocarlos@gmail.com","annagomez617@gmail.com","luis.zarzoso@gmail.com","mazuecos.raquel@gmail.com","jorzarso1989@gmail.com","beleninsnoo@gmail.com"]

lista_participantes2 = ['Abuelo','Abuela','Vicente','Rosa','Carlos','Anna','Luis','Raquel','Jorge','Belén']
for i in lista_participantes2:
    indice=lista_participantes2.index(i)
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = correo[indice]
    email["Subject"] = "Amic invisible"

 # Crear el contenido del correo en formato HTML con CSS
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
            }}
            h1 {{
                color: #333333;
            }}
            p {{
                color: #555555;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Amigo Invisible!</h1>
            <p>Hola {i},</p>
            <p>Vas a ser l'amic invisible de: {eleccion[indice]}</p>
            <p>¡Contesta al correu per a confirmar que l'has rebut!</p>
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




