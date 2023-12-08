from twilio.rest import Client
import numpy as np
from numpy.core.defchararray import index 

# Tus credenciales de Twilio
account_sid = 'tu_account_sid'
auth_token = 'tu_auth_token'
client = Client(account_sid, auth_token)

# Lista de participantes y restricciones
lista_participantes = ['Abuelo', 'Abuela', 'Vicente', 'Rosa', 'Carlos', 'Anna', 'Luis', 'Raquel', 'Jorge', 'Belén']
restricciones = {'Abuelo': ['Abuela'], 'Abuela': ['Abuelo'], 'Vicente': ['Rosa'], 'Rosa': ['Vicente'],
                 'Carlos': ['Anna'], 'Anna': ['Carlos'], 'Luis': ['Raquel'], 'Raquel': ['Luis'],
                 'Jorge': ['Belén'], 'Belén': ['Jorge']}

# Realizar el sorteo
eleccion = np.random.permutation(lista_participantes)
while any(x == y or y in restricciones.get(x, []) for x, y in zip(lista_participantes, eleccion)):
    eleccion = np.random.permutation(lista_participantes)

eleccion = eleccion.tolist()

# Enviar mensajes por WhatsApp
for i, participante in enumerate(lista_participantes):
    mensaje = f"¡Amigo Invisible!\nHola {participante},\nVas a ser el amigo invisible de: {eleccion[i]}\n¡Contesta para confirmar!"

    # Número de teléfono en formato E.164 (incluyendo el código de país, por ejemplo, +14155238886)
    numero_telefono = '+34617700732'

    # Enviar el mensaje por WhatsApp
    message = client.messages.create(
                              from_='whatsapp:+34617700732',
                              body=mensaje,
                              to=f'whatsapp:{numero_telefono}'
                          )

    print(f"Mensaje enviado a {participante} por WhatsApp.")
