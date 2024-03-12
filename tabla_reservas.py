import hashlib
import json

import pandas as pd


def hash_contrasena(pass_introducida):
    pass_bytes = pass_introducida.encode('utf-8')

    hasher = hashlib.sha256()
    hasher.update(pass_bytes)
    hash_ingresado = hasher.hexdigest()

    return hash_ingresado


def loadJSON():
    try:
        with open("new_usuarios.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def loadJSON2():
    try:
        with open("reservas.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


id_usuario = []
nombre = []
contraseña = []
new_usuarios = []
sala = []

reservasId = []
userid = []
salaId = []
plaza = []
suite = []
fecha_reserva = []
horas_reserva = []

usuarios = loadJSON()
reservas = loadJSON2()

for reserva in reservas:
    reservasId.append(reserva['reservaId']),
    userid.append(reserva['userId']),
    sala.append(reserva['sala'])
    fecha_reserva.append(reserva['date']),
    horas_reserva.append(reserva['hours']),

df = pd.DataFrame({
    'reservasId': reservasId,
    'userId': userid,
    'sala': sala,
    'date': fecha_reserva,
    'hours': horas_reserva,

})
df.to_excel("reserva.xlsx")
# pintamos df pues por la cara
print(df)
