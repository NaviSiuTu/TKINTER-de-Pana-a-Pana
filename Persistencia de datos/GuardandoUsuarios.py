import json

# Creamos un diccionario con usuarios y contraseñas
usuarios = {
    "ivan": "1234",
    "pepita": "abc123"
}

# Guardamos ese diccionario en un archivo llamado "usuarios.json"
with open("usuarios.json", "w") as archivo:
    json.dump(usuarios, archivo)

print("Listo: se guardaron los datos")
