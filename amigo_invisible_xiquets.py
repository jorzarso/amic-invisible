import numpy as np
from numpy.core.defchararray import index 
from email.message import EmailMessage
import smtplib

lista_participantes = ['Víctor','Marta','Anna','Àgueda','Mario','Pablo','Ningú!','Ningú!','Ningú!','Ningú!']
cantidad_participantes=len(lista_participantes)

    
eleccion = np.random.choice(lista_participantes,replace=False,size=cantidad_participantes)


eleccion = eleccion.tolist()
print(eleccion)

remitente = "jorzarso1989@gmail.com"
correo=["viczarbo@gmail.com","mariasorolla48@gmail.com","viczarzoso@gmail.com","rosamariagrso74@gmail.com","zarzosocarlos@gmail.com","annagomez617@gmail.com","luis.zarzoso@gmail.com","mazuecos.raquel@gmail.com","jorzarso1989@gmail.com","beleninsnoo@gmail.com"]


lista_participantes2 = ['Abuelo','Abuela','Vicente','Rosa','Carlos','Anna','Luis','Raquel','Jorge','Belén']
for i in lista_participantes2:
    indice=lista_participantes2.index(i)
    print(i+"-> "+eleccion[indice])
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = correo[indice]
    email["Subject"] = "Amic invisible xiquet"
    email.set_content("Seràs el amic invisible de: " + eleccion[indice])
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, "mgxpqyfjwcvlxekz")
    smtp.sendmail(remitente, correo[indice], email.as_string())
    smtp.quit()
