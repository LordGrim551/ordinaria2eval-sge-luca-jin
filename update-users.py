import hashlib
import json
import os


def hash_contrasena(pass_introducida):
    pass_bytes = pass_introducida.encode('utf-8')

    hasher = hashlib.sha256()
    hasher.update(pass_bytes)
    hash_ingresado = hasher.hexdigest()

    return hash_ingresado


new_usuarios = []
with open('usuarios.json', 'r', encoding='utf-8') as json_file:
    datos = json.load(json_file)

    for usuario in datos:

        nuevo_usuarios = {
            'nombre': usuario['id'],
            'password': hash_contrasena(usuario['password']),
            'id': len(new_usuarios)+1
        }
        new_usuarios.append(nuevo_usuarios)
    with open('secure-users.json', 'w') as json_out:
        json.dump(new_usuarios, json_out, indent=2)
