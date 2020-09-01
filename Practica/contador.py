import json

with open("Archivo2.json") as f:
    f = json.loads(f.read())
    contador = 0
    for registros in f:
        contador = contador +1
        print(contador)


