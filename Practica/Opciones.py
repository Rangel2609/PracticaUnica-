import json

import json
def cargar_datos(ruta):
    with open(ruta) as contenido:
        nombres = json.load(contenido)
        x = input("Escribe el nombre a encontrar")
        for z in nombres:
            y = z.get(x)
            print(min(y))
            return (y)
if __name__ == '__main__':
    ruta = "Archivo1.json"
    cargar_datos(ruta)






