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
    participante1: [participante2],
    participante2: [participante1],
    participante3: [participante4],
    participante4: [participante3],
    participante5: [participante6],
    participante6: [participante5],
    participante7: [participante8],
    participante8: [participante7],
    participante9: [participante10],
    participante10: [participante9]
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
    email.set_content("Seràs el amic invisible de: " + eleccion[indice])
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    # Password extra: gmail->seguridad->contraseñas de aplicaciones->Otra->Python->it must be put the password given by google
    # change mgxpqyfjwcvlxekz for the password commented
    smtp.login(remitente, "mgxpqyfjwcvlxekz")
    smtp.sendmail(remitente, correo[indice], email.as_string())
    smtp.quit()




