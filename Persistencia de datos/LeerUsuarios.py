import json

# Abrimos el archivo para leer los datos guardados
with open("usuarios.json", "r") as archivo:
    usuarios = json.load(archivo)

print("Estos son los usuarios guardados:")
print(usuarios)
