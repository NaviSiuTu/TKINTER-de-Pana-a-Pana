import json
import os

data = {
    
    "Nombre": "Ivan",
    "Edad": 22
}

#GUARDAR
with open("usuario.json", "w") as archivo:
    json.dump(data,archivo)

#LEER
with open("usuario.json", "r") as archivo:
    data = json.load(archivo)

print(data["Nombre"])
print(data["Edad"])

#CONVERTIR DICCIONARIO A TEXTO JSON

texto = json.dumps(data)
print(texto)

#CONVERTIR TEXTO JSON A DICCIONARIO


text = '{"Nombre": "Camilo", "Edad":30}'
datos = json.loads(text)

print(datos["Nombre"])
print(datos["Edad"])



#Agregar Usuarios a la base de datos

nuevo_usuario = {
    "Nombre": "Juan",
    "Edad": 25
}

archivo = "usuario.json"

if os.path.exists(archivo):
    with open(archivo, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []


data.append(nuevo_usuario)

with open (archivo, "w")as f:
    json.dump(data, f, indent=4)
