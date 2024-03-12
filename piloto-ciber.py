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




id_usuario = []
nombre = []
contraseña = []

new_usuarios = []

usuarios = loadJSON()



for usuario in usuarios:
    id_usuario.append(usuario['id']),
    nombre.append(usuario['nombre']),
    contraseña.append(usuario['password'])



df = pd.DataFrame({
    'nombre': nombre,
    'password': contraseña,
    'id_usuario':id_usuario
})

# pintamos df pues por la cara

print(df)


df.to_excel('usuarios.xlsx')

