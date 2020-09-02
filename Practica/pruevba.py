import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        z = int("Ingrese la ruta:")
        nombres = json.load(contenido)
        x = input("Ingrese el atributo")
        for nombre in nombres:
            edad = nombre.get('Edad')
            a = int(edad)

            print(min(a))
if __name__ == '__main__':
    ruta = "Archivo2.json"
    cargar_datos(ruta)


